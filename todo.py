import os
TODO_FILE = "tasks.txt"

def show_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")

def delete_task(index):
    tasks = show_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        with open(TODO_FILE, "w") as f:
            for task in tasks:
                f.write(task + "\n")

def main():
    while True:
        print("\n=== ToDoリスト ===")
        tasks = show_tasks()
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print("\n[a] 追加 / [d] 削除 / [q] 終了")
        cmd = input("操作を入力: ")

        if cmd == "a":
            task = input("追加するタスク: ")
            add_task(task)
        elif cmd == "d":
            idx = int(input("削除する番号: ")) - 1
            delete_task(idx)
        elif cmd == "q":
            break
        else:
            print("無効な操作です。")

if __name__ == "__main__":
    main()
