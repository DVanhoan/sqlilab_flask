# SQL Injection Mini-Lab (Flask + SQLite)

> Mục tiêu: Minh họa 3 ca SQLi kinh điển và cách fix "chuẩn doanh nghiệp": Login, Search, ORDER BY

## Cấu trúc
```
app/
  __init__.py
  config.py
  db.py
  blueprints/
    auth.py
    products.py
  services/
    user_service.py
    product_service.py
  templates/
    base.html
    login.html
    search.html
    products.html
  static/css/style.css
run.py
requirements.txt
```

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


