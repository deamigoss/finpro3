import streamlit as st
from sqlalchemy import text

list_montir = ['', 'Subagja', 'Andi', 'Karyono']
list_transmisi = ['', 'Matic', 'Cub']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://rizkiim198:5prbLmGT4qZk@ep-holy-snow-47509721.us-east-2.aws.neon.tech/finpro3")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS SERVICES (id serial, nama_montir varchar, nama_motor varchar, transmisi char(25), \
                                                       yang_ditangani text, harga_service_Rp varchar, servis_ke text, tanggal_pengerjaan date);')
    session.execute(query)

st.header('SIMPLE RECORD PEKERJAAN MONTIR')
page = st.sidebar.selectbox("Pilih Menu", ["View Data", "Search Data","Edit Data"])

##VIEW DATA
if page == "View Data":
    data = conn.query('SELECT * FROM services ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

##SEARCH DATA
if page == "Search Data":
    # Add search criteria
    search_criteria = st.sidebar.selectbox("Search by", ["-- Select Search Criteria --", "Montir", "Nama Customer", "Motor", "Tanggal Pengerjaan"])

    # Define an empty DataFrame for the search results
    search_results = pd.DataFrame()

    if search_criteria != "-- Select Search Criteria --":
        # Based on the selected criteria, get the search query from the user
        if search_criteria == "Montir":
            selected_montir = st.sidebar.selectbox("Select Montir", list_montir[1:])
            search_results = conn.query(f"SELECT * FROM services WHERE nama_montir = '{selected_montir}' ORDER BY id;", ttl="0").set_index('id')
        elif search_criteria == "Nama Customer":
            search_query = st.sidebar.text_input("Enter Nama Customer")
            if search_query:
                search_results = conn.query(f"SELECT * FROM services WHERE LOWER(nama_customer) LIKE LOWER('%{search_query}%') ORDER BY id;", ttl="0").set_index('id')
        elif search_criteria == "Motor":
            search_query = st.sidebar.text_input("Enter Motor")
            if search_query:
                search_results = conn.query(f"SELECT * FROM services WHERE LOWER(nama_motor) LIKE LOWER('%{search_query}%') ORDER BY id;", ttl="0").set_index('id')
        elif search_criteria == "Tanggal Pengerjaan":
            search_query = st.sidebar.time_input("Enter Tanggal Pengerjaan")
            if search_query:
                search_results = conn.query(f"SELECT * FROM services WHERE tanggal_pengerjaan = '{search_query}' ORDER BY id;", ttl="0").set_index('id')

        # Display search results
        st.dataframe(search_results)


#EDIT DATA
if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO services (nama_montir, nama_customer,nama_motor, transmisi, yang_ditangani, harga_service_Rp, servis_ke, waktu_pengerjaan_menit, tanggal_pengerjaan) \
                          VALUES (:1, :2,:3, :4, :5, :6, :7, :8, :9);')
            session.execute(query, {'1':'', '2':'','3':'', '4':'', '5':'[]', '6':'', '7':'', '8':'', '9':None})
            session.commit()

    data = conn.query('SELECT * FROM services ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        nama_montir_lama = result["nama_montir"]
        nama_customer_lama = result["nama_customer"]
        nama_motor_lama = result["nama_motor"]
        transmisi_lama = result["transmisi"]
        yang_ditangani_lama = result["yang_ditangani"]
        harga_servis_lama = result["harga_servis_Rp"]
        servis_ke_lama = result["servis_ke"]
        waktu_pengerjaan_lama = result["waktu_pengerjaan_menit"]
        tanggal_pengerjaan_lama = result["tanggal_pengerjaan"]

        with st.expander(f'a.n. {nama_montir_lama}'):
            with st.form(f'data-{id}'):
                nama_montir_baru = st.selectbox("nama_montir", list_montir, list_montir.index(nama_montir_lama))
                nama_customer_baru = st.text_input("nama_customer", nama_customer_lama)
                nama_motor_baru = st.text_input("nama_motor", nama_motor_lama)
                transmisi_baru = st.selectbox("transmisi", list_transmisi, list_transmisi.index(transmisi_lama))
                yang_ditangani_baru = st.multiselect("yang_ditangani", ["Perawatan", "Ganti Ban", "Ganti Oli", "Ganti Aki"], eval(yang_ditangani_lama))
                harga_servis_baru = st.text_input("harga_servis_Rp", harga_servis_lama)
                servis_ke_baru = st.text_input("servis_ke", servis_ke_lama)
                waktu_pengerjaan_baru = st.text_input("waktu_pengerjaan_menit", waktu_pengerjaan_lama)
                tanggal_pengerjaan_baru = st.date_input("tanggal_pengerjaan", tanggal_pengerjaan_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE services \
                                          SET nama_montir=:1, nama_customer=:2, nama_motor=:3, transmisi=:4, yang_ditangani=:5, \
                                          harga_servis_Rp=:6, servis_ke=:7, waktu_pengerjaan_menit=:8, tanggal_pengerjaan=:9 \
                                          WHERE id=:10;')
                            session.execute(query, {'1':nama_montir_baru, '2':nama_customer_baru, '3':nama_motor_baru, '4':transmisi_baru, '5':str(yang_ditangani_baru), 
                                                    '6':harga_servis_baru, '7':servis_ke_baru, '8':waktu_pengerjaan_baru, '9':tanggal_pengerjaan_baru, '10':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM services WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()