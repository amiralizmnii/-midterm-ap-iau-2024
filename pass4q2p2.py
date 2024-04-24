import random
import string


# تابعی برای تولید رمز عبور
def generate_password():
    # تعریف کاراکترهایی که می‌توان از آن‌ها انتخاب کرد
    numbers = string.digits  # اعداد
    special_chars = '@#'  # کاراکترهای خاص
    consonants_upper = ''.join(set(string.ascii_uppercase) - set('AEIOU'))  # حروف ساکن بزرگ
    consonants_lower = ''.join(set(string.ascii_lowercase) - set('aeiou'))  # حروف ساکن کوچک

    # اطمینان حاصل کنید که حداقل یک عدد، یک کاراکتر خاص و یک حرف کوچک گنجانده شده است
    password = [
        random.choice(numbers),  # انتخاب یک عدد تصادفی
        random.choice(special_chars),  # انتخاب یک کاراکتر خاص تصادفی
        random.choice(consonants_upper),  # انتخاب یک حرف ساکن بزرگ تصادفی
        random.choice(consonants_lower)  # انتخاب یک حرف ساکن کوچک تصادفی
    ]

    # باقیمانده رمز عبور را با حروف ساکن و اعداد تصادفی پر کنید
    while len(password) < random.randint(12, 19):  # انتخاب طول رمز عبور بین 12 تا 19 کاراکتر
        char = random.choice(consonants_upper + consonants_lower + numbers)  # انتخاب یک حرف ساکن یا عدد تصادفی
        password.append(char)  # افزودن حرف به رمز عبور

    # ترکیب کردن برای جلوگیری از الگوهای قابل پیش‌بینی
    random.shuffle(password)  # ترکیب کردن کاراکترها

    # تبدیل لیست به رشته
    return ''.join(password)  # تبدیل رمز عبور به یک رشته


# تولید و چاپ رمز عبور
print(generate_password())  # چاپ رمز عبور تولید شده
