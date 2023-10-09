def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v: str) -> float:
    v = float(v.removesuffix("ft"))
    return v*0.3048

if __name__ == "__main__":
    main()
