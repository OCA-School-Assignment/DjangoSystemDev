from django.db import models

JAPAN_PREFECTURES = [
    ('Hokkaido', '北海道'),
    ('Aomori', '青森'),
    ('Iwate', '岩手'),
    ('Miyagi', '宮城'),
    ('Akita', '秋田'),
    ('Yamagata', '山形'),
    ('Fukushima', '福島'),
    ('Ibaraki', '茨城'),
    ('Tochigi', '栃木'),
    ('Gunma', '群馬'),
    ('Saitama', '埼玉'),
    ('Chiba', '千葉'),
    ('Tokyo', '東京'),
    ('Kanagawa', '神奈川'),
    ('Niigata', '新潟'),
    ('Toyama', '富山'),
    ('Ishikawa', '石川'),
    ('Fukui', '福井'),
    ('Yamanashi', '山梨'),
    ('Nagano', '長野'),
    ('Gifu', '岐阜'),
    ('Shizuoka', '静岡'),
    ('Aichi', '愛知'),
    ('Mie', '三重'),
    ('Shiga', '滋賀'),
    ('Kyoto', '京都'),
    ('Osaka', '大阪'),
    ('Hyogo', '兵庫'),
    ('Nara', '奈良'),
    ('Wakayama', '和歌山'),
    ('Tottori', '鳥取'),
    ('Shimane', '島根'),
    ('Okayama', '岡山'),
    ('Hiroshima', '広島'),
    ('Yamaguchi', '山口'),
    ('Tokushima', '徳島'),
    ('Kagawa', '香川'),
    ('Ehime', '愛媛'),
    ('Kochi', '高知'),
    ('Fukuoka', '福岡'),
    ('Saga', '佐賀'),
    ('Nagasaki', '長崎'),
    ('Kumamoto', '熊本'),
    ('Oita', '大分'),
    ('Miyazaki', '宮崎'),
    ('Kagoshima', '鹿児島'),
    ('Okinawa', '沖縄'),
]

class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name


class Items(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'items'

    def __str__(self):
        return self.name
    

class Stock(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=100, choices=JAPAN_PREFECTURES)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'stock'

    def __str__(self):
        return self.item.name
    

class ShipmentLog(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    action = models.CharField(max_length=3, default=None)
    quantity = models.IntegerField(default=0)
    shipment_date = models.DateField(default=None)
    location = models.CharField(max_length=100, choices=JAPAN_PREFECTURES)

    class Meta:
        db_table = 'shipment_log'

    def __str__(self):
        return f'{self.item_id} - {self.action} - {self.location} - {self.quantity} - {self.shipment_date}'
        # return self.item.name


class Customer(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=8)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateField()
    estimated_delivery_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return str(self.id)    

class Production(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    lot_quantity = models.IntegerField()
    due_date = models.DateField()
    estimated_completion_date = models.DateField()
    completion_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'production'

    def __str__(self):
        return str(self.id)
    

