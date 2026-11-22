# make.fun entry — day-one freelance plan

Satu file Python tanpa dependensi yang menulis rencana hari pertama ke `/output/entry.txt`: tiga penawaran harga tetap di Fiverr dan Upwork (Python scraper $45, landing page $60, CSV cleanup $35), promosi $40 untuk yang paling laku, pengiriman dalam hitungan jam lewat kode, permintaan review setiap pembeli, dan kenaikan harga $5 tiap lima order — 12 order dalam 30 hari menghasilkan $540 bruto dan $440 neto.

## Cara jalan

Butuh Python 3.13 atau lebih baru (hanya pustaka standar, tanpa `pip install`).

```bash
python3 main.py
```

Skrip membuat folder `/output` bila belum ada, menulis tepat 276 karakter ke `/output/entry.txt`, lalu mencetak jumlah karakter yang ditulis. Isi teks ada di konstanta `TEXT` di dalam `main.py`; mengubahnya berarti mengubah entry-nya juga.
