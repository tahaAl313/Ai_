from typing import List, Dict

# --- بخش Preprocessing ---
MemoryEntry = Dict[str, object]
MemoryBank = List[MemoryEntry]

def normalize_text(text: str) -> str:
    text = text.strip()
    corrections = {
        "اموزظ": "آموزش",
        "اموزش": "آموزش",
        "اموز": "آموزش",
        "یاد 'رتم": "یاد گرفتم",
    }
    result = text
    for bad, good in corrections.items():
        result = result.replace(bad, good)
    return result

def normalize_importance(value: str) -> int:
    """تبدیل عدد (حتی عدد فارسی!) به int — با کمترین اعتماد به کاربر!"""
    # تبدیل ارقام فارسی/عربی به انگلیسی
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    arabic_digits = "٠١٢٣٤٥٦٧٨٩"
    for i, p in enumerate(persian_digits):
        value = value.replace(p, str(i))
    for i, a in enumerate(arabic_digits):
        value = value.replace(a, str(i))
    try:
        n = int(value)
    except ValueError:
        n = 5
        print("عدد معتبر نبود، عدد ۵ رو در نظر می‌گیریم.")
    return max(1, min(10, n))  # بین ۱ تا ۱۰ نگهش می‌داریم

def add_memory(bank: MemoryBank, text: str, topic: str, importance: int = 5) -> MemoryBank:
    entry = {"text": text, "topic": topic, "importance": int(importance)}
    bank.append(entry)
    return bank

def find_related(bank: MemoryBank, topic: str) -> MemoryBank:
    """خاطراتِ قدیمیِ مرتبط با این موضوع رو پیدا می‌کنه"""
    return [m for m in bank if m.get("topic") == topic]

def react_to_importance(importance: int) -> str:
    if importance >= 8:
        return "اوه! این خیلی مهمه! 🔥 حتماً باید روش کار کنیم!"
    elif importance >= 5:
        return "قشنگه! اتفاق خوبی به نظر می‌رسه. 👍"
    elif importance > 0:
        return "غمگینه؟ بشین بگیم تا حلش کنیم. 🤗"
    else:
        return "هیچی؟ خب، یه روز آرومِ. 😅"

def print_memory(bank: MemoryBank) -> None:
    print("\n🧠 لیست خاطراتِ ثبت شده:")
    for m in bank:
        print(f"✨ خاطره: {m['text']}")
        print(f"📌 موضوع: {m['topic']}")
        print(f"⚖️ اهمیت: {m['importance']}")
        print("-" * 20)

# --- کد اصلی ---
memory_bank = [
    {"text": "می‌خوام امنیتِ سیستم رو بسازم", "topic": "امنیت", "importance": 10},
    {"text": "امروز یاد گرفتم دیکشنری چیه", "topic": "آموزش", "importance": 8},
]

print("سلام طاها! سیستمِ حافظه و ارتباطِ خاطرات آماده‌ست. 😎")

new_text = input("\nطاها جان، چه خاطره‌ای داری؟ بنویس: ")
new_topic = normalize_text(input("موضوعش چیه؟: "))  # 🐛 فیکس: موضوع هم پاکسازی می‌شه!
importance = normalize_importance(
    input("چقدر برات مهمه؟ (۱ تا ۱۰، یا Enter برای ۵): ") or "5"
)

# 🎯 ارتباطِ خاطرات: قبل از ثبت، خاطرات قدیمیِ مرتبط رو چک می‌کنیم
related = find_related(memory_bank, new_topic)
if related:
    print(f"\n🤝 اوه طاها! من قبلاً {len(related)} خاطره درباره «{new_topic}» دارم:")
    for m in related:
        print(f"   ↔️ «{m['text']}»")
    print("پس این یکی به زنجیره‌ی خاطراتت وصل شد!")
else:
    print(f"\n🌱 این اولین خاطره‌ات درباره «{new_topic}» است. موضوع جدیدی شروع کردی!")

# ثبت نهایی
clean = normalize_text(new_text)
memory_bank = add_memory(memory_bank, clean, new_topic, importance)

print("\n✅ حافظه با موفقیت به‌روز شد!")
print(f"💬 واکنش برنامه: {react_to_importance(importance)}")
print_memory(memory_bank)
