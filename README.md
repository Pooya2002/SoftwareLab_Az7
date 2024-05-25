# SoftwareLab_Az7
# استقرار یک نرم‌افزار به کمک Docker
ابتدا در فایل settings.py تنظیمات مربوط به دیتابیس SQlite را به PostgreSQL تبدیل می‌کنیم (مطابق تصویر زیر)

![3](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/63320290-5e7c-426c-8b14-7694ba8c4d09)

حال فایل docker-compose.yml خود را با محتوای عکس زیر می‌سازیم.

![3 5](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/4b6ad208-65eb-491a-8643-acfd9fe68874)

برای بالا آوردن docker نیاز به ایجاد یک Dockerfile هم داریم. (تصویر زیر)

![27](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/4d4d379b-579b-4b32-bf5c-d678121d9d6f)


در ادامه مطابق تصویر زیر docker را بالا می‌آوریم.
![6](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/37ba9890-180d-46dd-94ae-29bb7e6f04fe)

![7](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/8776b20f-8e50-47a9-806d-1e70aa51423d)


حال عمل migration را انجام داده و دیتابیس را آپدیت می‌کنیم.

![8](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/fb3b661f-2f55-410b-8c2b-b7a606fc33d0)

![9](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/8d899392-805d-44b1-8f5e-8fe4cf45b523)

همانطور که در تصاویر زیر مشخص است برنامه توسط مرورگر قابل مشاهده است. اما برای درخواست دادن از طریق ترمینال (بدون استفاده از پنل ادمین) کد مشکلاتی از قبیل parse  نکردن درخواست json داشت که ابتدا آن‌ها را رفع کردیم.

![10](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/82332cb9-1bbd-4b9e-bc59-478c4c6df4bf)

![11](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/0a0fde26-2213-43c0-b7b2-d57a1d17bff4)

![12](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/1016a590-06f3-47c5-87de-8925f8b0b3ba)

![13](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/5f3c3fce-768a-42fe-812a-60515c6dc222)

به عنوان مثال برای ساخت کاربر کد user_create را به شکل زیر نوشتیم تا ابتدا درخواست را parse کند.


![15](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/8ff7972d-af8f-4400-b028-73f5580c8cc2)

مطابق تصویر زیر کاربر user1 را می‌سازیم.
![18](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/1f2d0ba1-15ad-49db-9cb9-75b16e40d244)

سپس لاگین کرده 

![19](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/8bd3aafb-647a-4683-89c8-c67ca45e574e)

و دو یادداشت خواسته شده را اضافه می‌کنیم.

![20](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/35ecc168-f391-4722-853e-0e38ceec1768)

لیست یادداشت ها در دستور زیر قابل مشاهده است.

![21](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/3dbed740-2391-4166-920b-16cc21f63945)

نوت اول که با id=3 ساخته شده را پاک کرده و دوباره لیست را نمایش میدهیم

![22](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/6456b258-cbc2-40f0-bd7f-eb6dbed7d2b9)

![23](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/027625c0-f165-4bc0-92d5-663d6d4ecb20)

با دستور زیر تمام Image ها را نمایش می‌دهیم. که notes-web و postgres مروبط به این آزمایش هستند.


![24](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/d074a2e2-c12a-47d9-bc60-ad008a2e2257)

لیست کانتینرها هم مطابق دستور زیر دریافت می‌کنیم. که همانطور که مشخص است اولی مربوط به web در پورت 8000 است. دومی مربوط به دیتابیس است.


![25](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/6be9c5cd-a0f9-45fd-aaac-ff15f373184f)

کانتینر مربوطه را از تصویر قبل استخراج کرده و با آن دو دستور ls و python --version را می‌زنیم.


![26](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/81496373-df7c-40d5-9d37-d0e29dd9a793)

