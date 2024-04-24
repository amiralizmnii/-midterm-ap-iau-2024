import random
import string

def generate_password():
    # تعریف مجموعه‌های کاراکتر
    uppercase_letters = string.ascii_uppercase  # حروف بزرگ (A-Z)
    digits = string.digits  # اعداد (0-9)
    special_characters = '@#'  # کاراکترهای ویژه (@ و #)
    consonants = ''.join(set(string.ascii_lowercase) - set('aeiou'))  # حروف ساکن (بدون حروف صدادار)

    # تولید یک رمز عبور تصادفی
    password_length = random.randint(12, 19)  # طول تصادفی بین 12 تا 19 کاراکتر
    password = random.choice(uppercase_letters)  # حداقل یک حرف بزرگ
    password += random.choice(digits)  # حداقل یک عدد
    password += random.choice(special_characters)  # حداقل یک کاراکتر ویژه

    # پر کردن کاراکترهای باقی‌مانده (بدون حروف بزرگ صدادار)
    remaining_length = password_length - len( password)
    for _ in range(remaining_length):
        # انتخاب تصادفی از  حروف ساکن، اعداد و کاراکترهای ویژه
        password += random.choice( consonants + digits + special_characters)

    # ترتیب دادن تصادفی به رمز عبور برای افزایش امنیت
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

# تولید و چاپ رمز عبور
generated_password = generate_password()
print(f"Password: {generated_password}")
