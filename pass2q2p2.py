import random
import string


# تابعی برای تولید رمز عبور
def generate_password():
    # تعریف کاراکترهایی که می‌توان از آن‌ها انتخاب کرد
    numbers = string.digits  # اعداد
    special_chars = '@#'  # کاراکترهای خاص
    consonants_lower = ''.join(set(string.ascii_lowercase) - set('aeiou'))  # حروف ساکن کوچک
    consonants_upper = ''.join(set(string.ascii_uppercase) - set('AEIOU'))  # حروف ساکن بزرگ

    # اطمینان حاصل کنید که حداقل یک عدد و یک کاراکتر خاص گنجانده شده است
    password = [
        random.choice(numbers),  # انتخاب یک عدد تصادفی
        random.choice(special_chars),  # انتخاب یک کاراکتر خاص تصادفی
        random.choice(consonants_upper)  # اطمینان حاصل کنید که حداقل یک حرف بزرگ وجود دارد
    ]

    # باقیمانده رمز عبور را با حروف ساکن تصادفی پر کنید
    while len(password) < random.randint(12, 19):  # انتخاب طول رمز عبور بین 12 تا 19 کاراکتر
        char_type = random.choice(['lower', 'upper'])  # تصمیم گیری تصادفی برای انتخاب حرف کوچک یا بزرگ
        if char_type == 'lower':
            char = random.choice(consonants_lower)
        else:
            char = random.choice(consonants_upper)
        password.append(char)  # افزودن حرف به رمز عبور

    # ترکیب کردن برای جلوگیری از الگوهای قابل پیش‌بینی
    random.shuffle(password)  # ترکیب کردن کاراکترها

    # تبدیل لیست به رشته
    return ''.join(password)  # تبدیل رمز عبور به یک رشته و بازگرداندن آن


# تولید و چاپ رمز عبور
print(generate_password())  # چاپ رمز عبور تولید شده
