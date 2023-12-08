drop table if exists services;
create table services (
	id serial,
	nama_montir text,
    nama_customer text,
	nama_motor text,
	transmisi text,
	yang_ditangani text,
	harga_servis_Rp text,
	servis_ke text,
	waktu_pengerjaan_menit text,
	tanggal_pengerjaan date
);

insert into services (nama_montir, nama_customer, nama_motor, transmisi, yang_ditangani, harga_servis_Rp, servis_ke, waktu_pengerjaan_menit, tanggal_pengerjaan)
values
	('Andi', 'Sulaiman', 'BeAT Sporty CBS ISS SPION PLUS', 'Matic', '["Perawatan", "Ganti Ban"]', 250000, 1, '32', '2023-11-26'),
	('Karyono', 'Abrar', 'NF11C1C M/T', 'Cub', '["Perawatan", "Ganti Oli"]', 200000, 5, '46', '2023-10-26'),
	('Karyono', 'Irvan Sukama', 'NEW SUPRA CW FI', 'Cub', '["Ganti Aki"]', 200000, 2, '25', '2023-11-26'),
	('Andi', 'Talitha Rifka', 'VARIO 125 CBS JKT SF DL', 'Matic', '["Perawatan"]', 100000, 3, '20', '2023-11-26'),
	('Subagja', 'Muhaimin','NEW SUPRA CW FI', 'Cub', '["Ganti Oli"]', 125000, 4, '25', '2023-11-26'),
	('Karyono', 'Coki Pardede','NF125TR3 M/T', 'Cub', '["Perawatan", "Ganti Oli", "Ganti Ban", "Ganti Aki"]', 450000, 6, '60', '2023-11-26'),
	('Andi', 'Mangjo','NEW VARIO TECHNO PGM FI', 'Matic', '["Perawatan"]', 100000, 1, '27', '2022-10-07'),
	('Subagja', 'Dewi Putri','ALL NEW VARIO 125 FI CBS', 'Matic', '["Ganti Oli", "Ganti Ban", "Ganti Aki"]', 350000, 2, '52', '2023-11-26'),
	('Andi', 'Sultan Maung','NEW REVO FIT MC', 'Cub', '["Perawatan"]', 100000, 3, '25', '2022-10-09'),
	('Karyono', 'Makanzi','NEW BEAT ESP CBS PLUS', 'Matic', '["Perawatan"]', 100000, 4, '26', '2022-10-11')
	;
	
