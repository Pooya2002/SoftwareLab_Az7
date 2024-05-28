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

## پرسش‌های مربوط به پروژه 

نوت اول که با id=3 ساخته شده را پاک کرده و دوباره لیست را نمایش میدهیم

![22](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/6456b258-cbc2-40f0-bd7f-eb6dbed7d2b9)

![23](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/027625c0-f165-4bc0-92d5-663d6d4ecb20)

با دستور زیر تمام Image ها را نمایش می‌دهیم. که notes-web و postgres مروبط به این آزمایش هستند.


![24](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/d074a2e2-c12a-47d9-bc60-ad008a2e2257)

لیست کانتینرها هم مطابق دستور زیر دریافت می‌کنیم. که همانطور که مشخص است اولی مربوط به web در پورت 8000 است. دومی مربوط به دیتابیس است.


![25](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/6be9c5cd-a0f9-45fd-aaac-ff15f373184f)

کانتینر مربوطه را از تصویر قبل استخراج کرده و با آن دو دستور ls و python --version را می‌زنیم.


![26](https://github.com/Pooya2002/SoftwareLab_Az7/assets/63359673/81496373-df7c-40d5-9d37-d0e29dd9a793)

## پرسش‌های کلی
### 1. 
### Dockerfile

 یک فایل متنی بوده که داخل آن با یک سینتکس ساده و قابل فهم دستورالعمل‌های ساخت Docker Image قرار داده شده است. (تعریف بعدی درباره‌ی image است)  این فایل اطلاعات بسیار مهمی را در برمی گیرد که برای راه اندازی داکر استفاده از آنها ضروری است. در واقع Dockerfile مشخص می‌کند که پشت Container ما چه سیستم عاملی قرار بگیرد، همینطور از چه زبان ها، متغیرهای محلی، پورت‌های شبکه یا غیره استفاده شود. و مهم‌تر از همه اینکه مشخص کند Container ما بعد از اینکه واقعا اجرا شد قرار است چه کاری انجام دهد.

### Image 

در واقع یک تصویر ازسیستم‌عامل اصلی است. تصاویر (images) داکر قالب‌ها یا تمپلیت‌های فقط خواندنی (read-only) هستند که حاوی دستورالعمل‌هایی برای ایجاد یک کانتینر هستند. یک تصویر Docker یک عکس فوری یا طرح اولیه از کتابخانه ها و وابستگی های مورد نیاز در داخل یک کانتینر برای اجرای یک برنامه است. گفتیم Dockerfile شامل یک سری دستورالعمل برای ساختن یک Image است، در حالی که Docker Image یک فایل قابل حمل است که شامل یک سری دستورالعمل بوده که مشخص می‌کند Container کدام کامپوننت‌های نرم افزاری را اجرا کند و اینکه چطور آنها اجرا شوند. همچنین، یک image می تواند برپایه و اساس image دیگری، تنها با برخی تنظیمات‌ اضافی تر باشد. برای مثال، ممکن است تصویری بسازید که بر پایه تصویر اوبونتو باشد، اما وب سرور آپاچی، اپلیکیشن مورد نظرتان و همچنین جزئیات پیکربندی مورد نیاز برای اجرای برنامه شما را نصب کند. وقتی Dockerfile را تغییر می‌دهید و تصویر را بازسازی می‌کنید، تنها لایه‌هایی که تغییر کرده‌اند بازسازی می‌شوند. این بخشی از چیزی است که تصاویر را در مقایسه با سایر فناوری های مجازی سازی بسیار سبک، کوچک و سریع می کند.


### Container 

کانتینر نمونه‌ای اجرایی و فعال از یک تصویر است. وقتی تصویر Docker اجرا می‌شود، نمونه‌ای از آن تصویر به شکل کانتینر درآمده و شروع به کار می‌کند. کانتینرها به اجرای برنامه‌ها در محیطی جدا شده کمک می‌کنند، به طوری که تداخل کمتری با سایر برنامه‌ها و خدمات در سیستم میزبان دارند. کانتینرها می‌توانند به سرعت شروع به کار و توقف کنند، و امکان مدیریت منابع (مانند CPU و حافظه) را به صورت جداگانه برای هر کانتینر فراهم می‌آورند. پس در مقایسه با image میتوان گفت Docker Images برای بسته بندی برنامه ها و محیط های سرور از پیش پیکربندی شده استفاده می شود. کانتینرها از اطلاعات سرور و یک سیستم فایل ارائه شده توسط یک تصویر برای عملکرد استفاده می کنند. می‌توانید با استفاده از Docker API یا CLI یک کانتینر ایجاد، شروع، توقف، حرکت یا حذف کنید. می‌توانید یک کانتینر را به یک یا چند شبکه متصل کنید، فضای ذخیره‌سازی را به آن متصل کنید، یا حتی یک تصویر جدید بر اساس وضعیت فعلی آن ایجاد کنید.

### 2.

### کاربردهای Kubernetes

 یک سیستم مدیریت کانتینرها است که در مقیاس بزرگ برای اتوماسیون استقرار، مقیاس‌بندی و مدیریت برنامه‌های کانتینری استفاده می‌شود. این ابزار امکانات متنوعی را فراهم می‌کند که شامل موارد زیر است:

  استقرار و مدیریت برنامه‌ها: Kubernetes به ما اجازه می‌دهد برنامه‌های کانتینری خود را به صورت خودکار deployو  مدیریت کنیم که شامل توزیع بار و ترافیک بین کانتینرها برای بهبود استفاده از منابع و دستیابی به بالاترین سطح دسترس‌پذیری می‌شود.
    
  مقیاس‌بندی خودکار: Kubernetes می‌تواند تعداد کانتینرها را بر اساس نیاز فعلی افزایش یا کاهش دهد، که این به بهینه‌سازی هزینه‌ها و کارایی کمک می‌کند.

  بهبود استقرار: با استفاده از روش‌های به روزرسانی پیوسته و رول‌بک خودکار در صورت بروز مشکل، Kubernetes اطمینان می‌دهد که نسخه‌های جدید برنامه به آسانی و با کمترین خطر جایگزین نسخه‌های قدیمی‌تر شوند.

  مدیریت مخزن‌داده و حافظه: ارائه سیستم‌های ذخیره‌سازی پایدار و ادغام آن‌ها با کانتینرها، برای حفظ داده‌ها حتی زمانی که کانتینرها ایجاد و حذف می‌شوند.

  وSelf-service و federation: اجازه دادن به توسعه‌دهندگان برای طراحی و مدیریت برنامه‌های خود با استفاده از واسط‌های خط فرمان و API‌ها.


### رابطه Kubernetes با Docker

دو فناوری مکمل هستند که برای مدیریت برنامه‌های کانتینری استفاده می‌شوند. Docker به عنوان پلتفرمی برای ساخت و اجرای کانتینرها عمل می‌کند، در حالی که Kubernetes یک ابزار برای مدیریت کانتینرهای متعدد در مقیاس بزرگ است. Kubernetes می‌تواند کانتینرهای ساخته شده توسط Docker و سایر پلتفرم‌های کانتینری مانند rkt و CRI-O را مدیریت کند.
به عبارت دیگر، نحوه ی کار کردن داکر و Kubernetes با یکدیگر را از این سه جنبه می توانیم بررسی کنیم:

1)
یکپارچه سازی زمان اجرا کانتینر: Kubernetes از یک Container Runtime برای مدیریت چرخه حیات کانتینرها استفاده می کند. در حالی که داکر زمان اجرای پیش‌فرض در روزهای اولیه Kubernetes بود، Container Runtime Interface (CRI) اکنون به Kubernetes اجازه می‌دهد تا از چندین زمان اجرا کانتینر، از جمله Containerd (جزء اصلی رانتایم داکر)  و موارد دیگر مانند CRI-O پشتیبانی کند.
 
2)
ساخت و اجرای کانتینرها:  توسعه دهندگان اغلب از Docker برای ساخت و اجرای کانتینرها به صورت محلی در طول توسعه استفاده می کنند. این تصاویر داکر سپس برای استفاده در تولید در یک خوشه Kubernetes مستقر می شوند. Kubernetes این تصاویر Docker را از یک رجیستری کانتینر (مانند  Docker Hub، Google Container Registry، و غیره) بیرون می‌کشد و آنها را طبق پیکربندی‌های مشخص شده مستقر می‌کند.
  
3)
مدیریت کانتینرها در مقیاس های مختلف: داکربه تنهایی می‌تواند کانتینرها را روی یک گره مدیریت کند، اما Kubernetes می‌تواند کانتینرها را در یک دسته از گره‌ها مدیریت کند. این زیرساخت زیربنایی را انتزاع می‌کند و قابلیت‌های ارکستراسیون پیشرفته، مانند مقیاس‌بندی خودکار، خوددرمانی، و به‌روزرسانی‌های چرخشی را ارائه می‌کند.
