from enhancer import enhance_prompt

def main():
    while True:
      raw_prompt = input("Enter your raw prompt (or 'exit' to quit): ")
      if raw_prompt.lower() == 'exit':
        break

      enhanced_prompt = enhance_prompt(raw_prompt)
      print("\nEnhanced Prompt:\n")
      print(enhanced_prompt)
      print("-" * 40)

if __name__ == "__main__":
    main()