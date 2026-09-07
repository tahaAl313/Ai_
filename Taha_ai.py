# قدم اول: تعریف کردنِ بانکِ حافظه (داده‌ها)
memory_bank = [
    {"text": "می‌خوام امنیتِ سیستم رو بسازم", "topic": "امنیت", "importance": 10},
    {"text": "امروز یاد گرفتم دیکشنری چیه", "topic": "آموزش", "importance": 8},
    {"text": "می خوام یاد بگیرم", "topic": "آموزش", "importance": 8}
]

# قدم دوم: استفاده از حلقه برای مرورِ داده‌ها
# معنی این دستور اینه: "برایِ هر کدوم از خاطرات توی لیستِ memory_bank، این کارها رو انجام بده"
for memory in memory_bank:
    print(f"خاطره: {memory['text']}")
    print(f"موضوع: {memory['topic']}")
    print("---") # این فقط یه خط‌چین برای زیباییه
for memory in memory_bank:
    if memory['topic'] == "آموزش":
        print(f"📖 موردِ آموزشی: {memory['text']}")
# این همون بانک حافظه‌ی اولیه
memory_bank = [
    {"text": "می‌خوام امنیتِ سیستم رو بسازم", "topic": "امنیت", "importance": 10}
]

# ۱. دریافتِ ورودی از تو (طاها)
new_text = input("طاها، چه خاطره‌ای داری؟ بنویس: ")
new_topic = input("موضوعش چیه؟ (مثلاً آموزش یا امنیت): ")

# ۲. اضافه کردنِ خاطره‌ی جدید به بانک
# با دستورِ .append() می‌گیم: «بچسبونش به انتهای لیست!»
new_memory = {"text": new_text, "topic": new_topic, "importance": 5}
memory_bank.append(new_memory)

print("\n--- بانکِ حافظه به‌روزرسانی شد ---")
print(memory_bank)

user_input = "اموزظ"
cleaned_input = user_input . replace("اموزظ", "آموزش").replace("اموزش", "آموزش").replace("اموزش", "آموزش") 

print(f"ورودی اولیه  :{user_input}")
print(f"ورودی تمیز شده: {cleaned_input}")


if cleaned_input == "آموزش":
    print("این یک خاطره آموزشی است!")
else:
    print("این خاطره ربطی به آموزش ندارد.")
