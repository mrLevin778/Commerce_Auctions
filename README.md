# Commerce_Auctions
Commerce
Спроєктуйте подібний до eBay онлайн-майданчик для електронної торгівлі та проведення аукціонів, на якому користувачі зможуть виставляти товари, розміщувати ставки та додавати товари до списку відстеження.

Active listings page

Listing page

Перші кроки
Завантажте дистрибутив з https://cdn.cs50.net/web/2020/spring/projects/2/commerce.zip і розпакуйте його.
У вашому терміналі виконайте cd у директорію commerce.
Виконайте python manage.py makemigrations auctions щоб створити міграції для застосунку auctions.
Виконайте python manage.py migrate щоб застосувати міграції до вашої бази даних.
Пояснення
У дистрибутиві знаходиться Django-проєкт під назвоюcommerce, в якому міститься один застосунок auctions.

Спочатку відкрийте auctions/urls.py, де визначено URL-конфігурацію для цього застосунку. Зверніть увагу, що ми вже написали для вас кілька URL, включно з типовим індексним маршрутом, а також маршрутами /login, /logout і /register.

Зазирніть до auctions/views.py, щоб побачити види, пов’язані з кожним з цих маршрутів. Поки що представлення index повертає майже пустий шаблон index.html. Представлення login_view відображає форму входу в обліковий запис для користувача, що пробує отримати сторінку методом GET. Коли користувач надішле форму за допомогою запиту POST, його буде автентифіковано, відбудеться вхід в обліковий запис і користувача перенаправлять на головну сторінку. Представлення logout_view здійснює вихід користувача з облікового запису і перенаправляє його на сторінку. Насамкінець, маршрут register показує користувачу форму реєстрації та створює нового користувача після надання заповненої форми. Все це вже зроблено для вас, тож ви повинні мати змогу одразу запустити застосунок для створення користувачів.

Виконайте python manage.py runserver щоб розпочати роботу вебсеревера Django, і зайдіть на сайт у своєму браузері. Натисніть «Зареєструватися» і зареєструйтеся для отримання облікового запису. Ви побачите, що ви тепер маєте позначку «Ви увійшли як» у вашому обліковому записі і що посилання вгорі сторінки змінилися. Як змінився HTML? Подивіться в auctions/templates/auctions/layout.html щоб побачити HTML-макет цього застосунку. Зверніть увагу, що чимало частин шаблону оточені перевіркою чи user.is_authenticated,щоб залежно від того, увійшов користувач в обліковий запис, чи ні, йому було показано різне наповнення. Ви можете змінити цей файл, якщо хочете щось додати чи змінити в макеті!

Насамкінець подивіться в auctions/models.py. Саме тут ви визначатимете будь-які моделі для вашого застосунку, кожна з яких представлятиме певний тип даних, котрі ви хочете зберегти у вашій базі даних. Ми вже зробили для вас модель User, що представляє кожного користувача застосунку. Оскільки вона наслідує від AbstractUser, то вона вже має поля для імені користувача, електронної пошти, паролю та ін., але ви можете додати й інші поля до класу User, якщо ви хочете представити якусь додаткову інформацію про користувача. Вам також потрібно буде доповнити цей файл додатковими моделями, щоб представити деталі категорій та аукціонів, ставок і коментарів. Пам’ятайте, що щоразу, як ви змінюватимете щось в auctions/models.py, вам потрібно буде спочатку виконати python manage.py makemigrations, а потім python manage.py migrate, щоб перенести ці зміни до вашої бази даних.

Специфікація завдання
Завершіть реалізацію вашого сайту для проведення аукціонів з урахуванням таких вимог:

Моделі: Ваш застосунок повинен мати щонайменше три моделі на додачу до моделі User: для аукціонів, ставок і коментарів до аукціонів. Вам вирішувати, які поля мають бути в кожній моделі і яких типів мають бути ці поля. Ви можете створити додаткові моделі, якщо захочете.
Створення аукціону: Користувачі повинні мати змогу зайти на сторінку, щоб створити новий аукціон. У них має бути можливість вказати назву товару, надати текстовий опис і зазначити, якою має бути початкова ставка. Також користувачі повинні мати можливість за бажанням надати URL для зображення товару та/або категорії (як-от Мода, Іграшки, Електроніка, Дім тощо).
Сторінка активних аукціонівe: Типовий маршрут вашого вебзастосунку має дозволити користувачам переглянути всі активні аукціони. Для кожного активного аукціону ця сторінка має відображати щонайменше назву, опис, поточну ціну і фото товару (якщо воно існує).
Сторінка аукціону: Натискання на аукціон має переносити користувача на сторінку, присвячену цьому аукціону. На цій сторінці користувач повинен мати змогу переглянути усі деталі товару, включно з поточною ціною.
Якщо користувач увійшов до облікового запису, він має отримати можливість додати товар до списку відстеження «Watchlist». Якщо товар вже знаходиться в цьому списку, користувач повинен мати змогу видалити його.
Якщо користувач увійшов до облікового запису, він повинен мати можливість зробити ставку на товар. Ставка має бути не меншою за початкову ставку і більшою за будь-які інші ставки, що вже були розміщені (якщо такі існують). Якщо ставка не відповідає цим критеріям, користувач має отримати повідомлення про помилку.
Якщо користувач увійшов до облікового запису і він є автором аукціону, він повинен мати змогу «закрити» аукціон на цій сторінці, що зробить автора найбільшої ставки переможцем аукціону, а сам аукціон стане неактивним.
Якщо користувач увійшов до облікового запису на сторінці закритого аукціону і він є переможцем цього аукціону, він має отримати повідомлення про це.
Користувачі, які увійшли до облікових записів, повинні мати можливість додавати коментарі на сторінці аукціону. Сторінка аукціону має відображати всі коментарі, які було зроблено щодо цього аукціону.
Список відстеження: Користувачі, які увійшли до облікових записів, повинні мати змогу зайти на сторінку списку відстеження, яка, своєю чергою, повинна відображати всі аукціони, які користувач додав до свого списку. Натискання на будь-який з цих аукціонів має переносити користувача на сторінку відповідного аукціону.
Категорії: Користувачі повинні мати змогу зайти на сторінку, що відображає список усіх категорій аукціонів. Натискання на назву категорії має переносити користувача на сторінку, що показує всі активні аукціони цієї категорії.
Інтерфейс Django Admin: За допомогою інтерфейсу адміністратора Django адміністратор сайту повинен мати змогу переглянути, додати, змінити чи видалити будь-які аукціони, коментарі й ставки, зроблені на сайті.
Підказки
Створіть суперкористувача, що отримає доступ до інтерфейсу Django Admin: python manage.py createsuperuser.
Зверніться до Довідника типів полів Django за інформацією про можливі типи полів для вашої моделі Django.
Вам, ймовірно, знадобиться створити кілька форм Django для різних частин цього вебзастосунку.
Додавши декоратор @login_required угорі кожного представлення, ви зробите так, щоб лише користувачі, що увійшли до облікових записів, отримали доступ до цих представлень.
Ви можете змінювати CSS за власним бажанням, щоб зробити ваш сайт унікальним! На початку сторінки ми показали вам кілька скріншотів для прикладу. Це лише приклади: ваші застосунки не мають бути схожими на ці скріншоти – ми закликаємо вас бути креативними!
Нагадуємо, що завдання у цьому курсі розраховані на ваше самостійне виконання, але закликаємо вас ділитись готовими застосунками на форумі курсу та обговорювати зі співслухачами. Якщо у вас виникнуть питання щодо виконання, ви також можете поставити їх на форумі.
