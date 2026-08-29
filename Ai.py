secret_password = "taha"
attempts = 0

while True:
    user_input = input("رمز عبور را وارد کنید: ")

    if user_input.lower() == secret_password.lower():
        print("رمز صحیح خوش آمدید")
        break
    else:
        attempts += 1
        print(f"رمز اشتباه بود این تلاش شماره {attempts} بود")

        if attempts == 2:
            print("ی راهنمایی اول رمز با 't' شروع میشه")

        if attempts >= 5:
            print("بیش از حد تلاش کردی سیستم قفل شد")
            break
          
