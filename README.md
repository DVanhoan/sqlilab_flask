# SQL Injection Mini-Lab (Flask + SQLite)

## Cách chạy
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
# mở http://localhost:5000
```


## Data mẫu
- Users: `admin/1234`, `user/abcd`
- Products: một số sản phẩm phổ biến với giá tham khảo

## Các trang
- Vulnerable:
  - `/vuln/login`
  - `/vuln/search`
  - `/vuln/products?order=...`
- Safe:
  - `/safe/login`
  - `/safe/search`
  - `/safe/products?order=...` (whitelist: id, name, price)


