def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1]

    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    total_waiting_time = sum(waiting_time)
    average_waiting_time = total_waiting_time / n
    total_turnaround_time = sum(turnaround_time)
    average_turnaround_time = total_turnaround_time / n

    print("프로세스\t대기 시간\t반환 시간")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\n전체 대기 시간: {total_waiting_time}")
    print(f"평균 대기 시간: {average_waiting_time:.2f}")
    print(f"전체 반환 시간: {total_turnaround_time}")
    print(f"평균 반환 시간: {average_turnaround_time:.2f}")
  
def sjf(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    processes.sort(key=lambda x: x[1])  # 실행 시간을 기준으로 프로세스 정렬

    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1]

    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    total_waiting_time = sum(waiting_time)
    average_waiting_time = total_waiting_time / n
    total_turnaround_time = sum(turnaround_time)
    average_turnaround_time = total_turnaround_time / n

    print("프로세스\t대기 시간\t반환 시간")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\n전체 대기 시간: {total_waiting_time}")
    print(f"평균 대기 시간: {average_waiting_time:.2f}")
    print(f"전체 반환 시간: {total_turnaround_time}")
    print(f"평균 반환 시간: {average_turnaround_time:.2f}")

def hrn(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    response_ratio = [0] * n

    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1]

    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]
        response_ratio[i] = float(turnaround_time[i]) / processes[i][1]

    total_waiting_time = sum(waiting_time)
    average_waiting_time = total_waiting_time / n
    total_turnaround_time = sum(turnaround_time)
    average_turnaround_time = total_turnaround_time / n

    print("프로세스\t대기 시간\t반환 시간\t응답 비율")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\t\t{response_ratio[i]:.2f}")

    print(f"\n전체 대기 시간: {total_waiting_time}")
    print(f"평균 대기 시간: {average_waiting_time:.2f}")
    print(f"전체 반환 시간: {total_turnaround_time}")
    print(f"평균 반환 시간: {average_turnaround_time:.2f}")

a = input(' 1. FCFS \n 2. SJF \n 3. HRN\n')

n = int(input("프로세스의 갯수를 입력하세요: "))

processes = []
for i in range(n):
    name = i + 1
    burst_time = int(input(f"프로세스 {i+1}의 작업 시간을 입력하세요: "))
    processes.append((name, burst_time))

if a == '1':
  fcfs(processes)
elif a == '2':
  sjf(processes)
else :
  hrn(processes)
