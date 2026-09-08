from typing import List, Dict

# --- کدهای بخش Preprocessing ---
MemoryEntry = Dict[str, object]
MemoryBank = List[MemoryEntry]

def normalize_text(text: str) -> str:
    corrections = {
        "اموزظ": "آموزش",
        "اموزش": "آموزش",
        "اموز": "آموزش",
    }
    result = text
    for bad, good in corrections.items():
        result = result.replace(bad, good)
    return result

def add_memory(bank: MemoryBank, text: str, topic: str, importance: int = 5) -> MemoryBank:
    entry = {"text": text, "topic": topic, "importance": int(importance)}
    bank.append(entry)
    return bank

def print_memory(bank: MemoryBank) -> None:
    for m in bank:
        print(f"خاطره: {m['text']}")
        print(f"موضوع: {m['topic']}")
        print("---")

# --- کد اصلی برنامه ---
# بانک حافظه اولیه
memory_bank = [
    {"text": "می‌خوام امنیتِ سیستم رو بسازم", "topic": "امنیت", "importance": 10},
    {"text": "امروز یاد گرفتم دیکشنری چیه", "topic": "آموزش", "importance": 8},
    {"text": "می خوام یاد بگیرم", "topic": "آموزش", "importance": 8},
]

print("حافظه فعلی:")
print_memory(memory_bank)

# دریافت ورودی از تو (طاها)
new_text = input("طاها جان، چه خاطره‌ای داری؟ بنویس: ")
new_topic = input("موضوعش چیه؟ (مثلاً آموزش یا امنیت): ")

# پردازش و افزودن
clean = normalize_text(new_text)
memory_bank = add_memory(memory_bank, clean, new_topic, 5)

print("\n--- بانک حافظه به‌روزرسانی شد ---")
print_memory(memory_bank)

