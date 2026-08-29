secret_password = "taha"

while True:
    user_input = input("رمز عبور را وارد کنید: ")

    if user_input == secret_password:
        print("رمز صحیح خوش آمدید")
        break
    else:
        print("اوه اوه! رمز اشتباه دباره تلاش کن")
      
