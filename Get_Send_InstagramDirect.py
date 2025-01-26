import requests  # برای ارسال درخواست‌ها به API از این ماژول استفاده می‌کنیم.

# تابع برای ارسال پیام در دایرکت اینستاگرام
def send_direct_message(boxapi_username, boxapi_password, instagram_username, instagram_password, text, user_ids=None, thread_ids=None):
    """
    ارسال پیام دایرکت به کاربران یا گفتگوها.
    """
    url = "https://di.boxapi.ir/api/direct_send"  # آدرس API برای ارسال پیام
    auth = (boxapi_username, boxapi_password)  # احراز هویت با استفاده از نام کاربری و رمز عبور BoxAPI
    payload = {
        "username": instagram_username,  # نام کاربری اینستاگرام
        "password": instagram_password,  # رمز عبور اینستاگرام
        "text": text,  # متن پیام
        "user_ids": user_ids or [],  # لیست شناسه کاربران (در صورت وجود)
        "thread_ids": thread_ids or []  # لیست شناسه گفتگوها (در صورت وجود)
    }
    # ارسال درخواست POST به API
    response = requests.post(url, auth=auth, json=payload)
    return response.json()  # بازگرداندن پاسخ API به صورت JSON


# تابع برای دریافت تمامی چت‌ها و پیام‌ها
def get_all_threads(boxapi_username, boxapi_password, instagram_username, instagram_password, thread_id=0, amount=20):
    """
    دریافت لیست کامل چت‌ها و پیام‌ها.
    """
    url = "https://di.boxapi.ir/api/direct_thread"  # آدرس API برای دریافت لیست چت‌ها
    auth = (boxapi_username, boxapi_password)  # احراز هویت
    payload = {
        "username": instagram_username,  # نام کاربری اینستاگرام
        "password": instagram_password,  # رمز عبور اینستاگرام
        "thread_id": thread_id,  # شناسه گفتگو (0 برای همه چت‌ها)
        "amount": amount  # تعداد پیام‌هایی که باید دریافت شود
    }
    # ارسال درخواست POST به API
    response = requests.post(url, auth=auth, json=payload)
    return response.json()  # بازگرداندن پاسخ API به صورت JSON


# تابع برای دریافت پیام‌های یک چت خاص
def get_specific_thread_messages(boxapi_username, boxapi_password, instagram_username, instagram_password, thread_id, amount=20):
    """
    دریافت پیام‌های یک چت خاص.
    """
    url = "https://di.boxapi.ir/api/direct_messages"  # آدرس API برای دریافت پیام‌های یک چت
    auth = (boxapi_username, boxapi_password)  # احراز هویت
    payload = {
        "username": instagram_username,  # نام کاربری اینستاگرام
        "password": instagram_password,  # رمز عبور اینستاگرام
        "thread_id": thread_id,  # شناسه گفتگو
        "amount": amount  # تعداد پیام‌هایی که باید دریافت شود
    }
    # ارسال درخواست POST به API
    response = requests.post(url, auth=auth, json=payload)
    return response.json()  # بازگرداندن پاسخ API به صورت JSON


# مثال استفاده از توابع
if __name__ == "__main__":
    # تعریف اطلاعات کاربری
    boxapi_username = "boxapi_username"  # نام کاربری BoxAPI
    boxapi_password = "boxapi_password"  # رمز عبور BoxAPI
    instagram_username = "your_instagram_username"  # نام کاربری اینستاگرام
    instagram_password = "your_instagram_password"  # رمز عبور اینستاگرام

    # ارسال پیام
    result_send = send_direct_message(
        boxapi_username, boxapi_password,
        instagram_username, instagram_password,
        "سلام! این یک پیام تستی است.",  # متن پیام
        user_ids=["user_id_1"]  # شناسه کاربران هدف
    )
    print("نتیجه ارسال پیام:", result_send)

    # دریافت تمامی چت‌ها
    result_threads = get_all_threads(
        boxapi_username, boxapi_password,
        instagram_username, instagram_password
    )
    print("لیست چت‌ها:", result_threads)

    # دریافت پیام‌های یک چت خاص
    result_specific = get_specific_thread_messages(
        boxapi_username, boxapi_password,
        instagram_username, instagram_password,
        thread_id=123456  # شناسه چت مورد نظر
    )
    print("پیام‌های چت خاص:", result_specific)
