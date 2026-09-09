from typing import List, Dict

# اول باید نوع داده‌ها رو تعریف کنیم تا تابع بفهمه با چی کار می‌کنه
MemoryEntry = Dict[str, object]
MemoryBank = List[MemoryEntry]

def search_by_keywords(bank: MemoryBank, keywords: List[str]) -> MemoryBank:
    """
    خاطراتی را که حاوی حداقل یکی از کلمات کلیدی هستند، جستجو می‌کند.
    """
    found_memories = []
    for memory in bank:
        # کلمات کلیدی را به حروف کوچک تبدیل می‌کنیم
        normalized_keywords = [kw.lower() for kw in keywords]
        
        # متن و موضوع خاطره را هم به حروف کوچک تبدیل می‌کنیم
        memory_text_lower = memory.get("text", "").lower()
        memory_topic_lower = memory.get("topic", "").lower()
        
        # بررسی می‌کنیم که آیا کلمه کلیدی در متن یا موضوع هست یا نه
        for keyword in normalized_keywords:
            if keyword in memory_text_lower or keyword in memory_topic_lower:
                found_memories.append(memory)
                break # پیدا شد، پس بریم سراغ خاطره بعدی
                
    return found_memories

# --- بخش اجرایی برنامه (اینجا دیگه نباید داخل تابع باشه) ---

# ۱. ساخت بانک حافظه
memory_bank = [
    {"text": "می‌خوام امنیتِ سیستم رو بسازم", "topic": "امنیت", "importance": 10},
    {"text": "امروز یاد گرفتم دیکشنری چیه", "topic": "آموزش", "importance": 8},
    {"text": "یادگیری پایتون آسونه", "topic": "آموزش", "importance": 7},
    {"text": "حلقه for در پایتون", "topic": "برنامه‌نویسی", "importance": 6},
]

# ۲. تعیین کلمات برای جستجو
keywords_to_search = ["پایتون", "آموزش"]

# ۳. اجرای تابع جستجو
results = search_by_keywords(memory_bank, keywords_to_search)

# ۴. چاپ نتایج
print("\n--- نتایج جستجو با کلمات کلیدی ---")
if results:
    for res in results:
        print(f"✨ خاطره: {res['text']} (موضوع: {res['topic']}, اهمیت: {res['importance']})")
else:
    print("موردی یافت نشد.")
from typing import List, Dict

# --- کدهای بخش Preprocessing (با واکنش احساسی) ---
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

def add_memory(bank: MemoryBank, text: str, topic: str, importance: int = 5) -> MemoryBank:
    entry = {"text": text, "topic": topic, "importance": int(importance)}
    bank.append(entry)
    return bank

def react_to_importance(importance: int) -> str:
    """واکنش احساسی برنامه بر اساس میزان اهمیت"""
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

# --- کد اصلی برنامه ---
memory_bank = [
    {"text": "می‌خوام امنیتِ سیستم رو بسازم", "topic": "امنیت", "importance": 10},
    {"text": "امروز یاد گرفتم دیکشنری چیه", "topic": "آموزش", "importance": 8},
]

print("سلام طاها! سیستمِ حافظه آماده‌ست. 😎")
print_memory(memory_bank)

new_text = input("\nطاها جان، چه خاطره‌ای داری؟ بنویس: ")
new_topic = input("موضوعش چیه؟: ")

# اینجا کاربر خودش می‌تونه اهمیتش رو مشخص کنه (بین ۱ تا ۱۰)
try:
    importance = int(input("چقدر برات مهمه؟ (از ۱ تا ۱۰، یا Enter برای عدد ۵): ") or 5)
    if importance < 1: importance = 1
    if importance > 10: importance = 10
except ValueError:
    importance = 5
    print("عدد معتبر نبود، عدد ۵ رو در نظر می‌گیریم.")

clean = normalize_text(new_text)
memory_bank = add_memory(memory_bank, clean, new_topic, importance)

print("\n✅ حافظه با موفقیت به‌روز شد!")
print(f"💬 واکنش برنامه: {react_to_importance(importance)}")
print_memory(memory_bank)
