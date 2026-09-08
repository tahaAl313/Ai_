# preprocessing.py
from typing import List, Dict

# نمونهٔ سادهٔ بانک حافظه به‌صورت برگرفته از داده‌های شما
MemoryEntry = Dict[str, object]
MemoryBank = List[MemoryEntry]

def normalize_text(text: str) -> str:
    """
    ساده‌ترین سطحِ پیش‌پردازش: اصلاح برخی غلط‌های املایی رایج
    و بازگردانی متن به شکل یکسان (مختصرسازی کاراکترها).
    در مرحلهٔ بعد می‌تونیم از دیکشنری اصلاح‌کننده و توابع پیچیده‌تر استفاده کنیم.
    """
    corrections = {
        "اموزظ": "آموزش",
        "اموزش": "آموزش",
        "اموز": "آموزش",
        # اضافه کنید هر بار که دیدید ;)
    }
    result = text
    for bad, good in corrections.items():
        result = result.replace(bad, good)
    # می‌تونیم اعمالِ بیشتر مثل نرمال‌سازی فاصله‌ها رو هم اضافه کنیم
    return result

def add_memory(bank: MemoryBank, text: str, topic: str, importance: int = 5) -> MemoryBank:
    """افزودن خاطره به بانک حافظه با اعتبارسنجی ساده"""
    entry = {"text": text, "topic": topic, "importance": int(importance)}
    bank.append(entry)
    return bank

def print_memory(bank: MemoryBank) -> None:
    for m in bank:
        print(f"خاطره: {m['text']}")
        print(f"موضوع: {m['topic']}")
        print("---")

def filter_by_topic(bank: MemoryBank, topic: str) -> MemoryBank:
    return [m for m in bank if m.get("topic") == topic]

# نمونهٔ استفاده در همین فایل برای نمایش (بعداً از اصلی پروژه جدا کنید)
if __name__ == "__main__":
    memory_bank = [
        {"text": "می‌خوام امنیتِ سیستم رو بسازم", "topic": "امنیت", "importance": 10},
        {"text": "امروز یاد گرفتم دیکشنری چیه", "topic": "آموزش", "importance": 8},
        {"text": "می خوام یاد بگیرم", "topic": "آموزش", "importance": 8},
    ]

    print("قبل از بروزرسانی:")
    print_memory(memory_bank)

    # نمونهٔ اضافه‌کردن با ورودی‌های فرضی
    memory_bank = add_memory(memory_bank, "یادگیری پایتون با پروژه", "آموزش", 6)

    print("\nبعد از بروزرسانی:")
    print_memory(memory_bank)

    # نمونهٔ تمیزکاریِ ورودیِ تازه
    raw_input = "اموزظ"
    cleaned = normalize_text(raw_input)
    print("\nورودی اولیه:", raw_input)
    print("ورودی تمیز شده:", cleaned)
# main.py
from preprocessing import memory_bank as _memory_bank, add_memory, normalize_text, print_memory, filter_by_topic

memory_bank = _memory_bank.copy()  # یا از یک فایل ذخیره‌سازی استفاده کن

# ورودی کاربر
new_text = input("طاها، چه خاطره‌ای داری؟ بنویس: ")
new_topic = input("موضوعش چیه؟ (مثلاً آموزش یا امنیت): ")

# پیش‌پردازش و افزودن به حافظه
clean = normalize_text(new_text)
memory_bank = add_memory(memory_bank, clean, new_topic, 5)

print("\n--- بانک حافظه به‌روزرسانی شد ---")
print_memory(memory_bank)

