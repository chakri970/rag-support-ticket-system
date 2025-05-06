from retriever import load_tickets, build_index, search_tickets
from generator import generate_response


def main():
    print("🔍 RAG Support Ticket Search")
    tickets = load_tickets()
    index, _ = build_index(tickets)

    while True:
        query = input("\nEnter your support query (or type 'exit'): ").strip()
        if query.lower() == "exit":
            break

        results = search_tickets(query, index, tickets)
        print("\n📎 Relevant Tickets:")
        for t in results:
            print(f"- {t['title']}: {t['resolution']}")

        print("\n💬 Suggested Response:")
        response = generate_response(query, results)
        print(response)

        # ✅ Feedback mechanism
        feedback = input(
            "\nWas this response helpful? (y/n): ").strip().lower()
        if feedback in ['y', 'n']:
            with open("feedback_log.txt", "a") as f:
                f.write(
                    f"Query: {query}\nResponse: {response}\nFeedback: {feedback}\n{'-'*40}\n")

            if feedback == 'y':
                print("✅ Thanks for your feedback!")
            else:
                print("⚠️ Sorry the response wasn't helpful. Feedback noted.")
        else:
            print("❓ Feedback not understood. Skipping feedback log.")

        print("\n" + "-"*50)


if __name__ == "__main__":
    main()
