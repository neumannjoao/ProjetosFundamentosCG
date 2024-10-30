class Process:
    def __init__(self, pid):
        self.pid = pid

    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")


class ComputingProcess(Process):
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression

    def execute(self):
        try:
            result = eval(self.expression)  # Cuidado com eval em produção!
            print(f"Resultado da expressão {self.expression}: {result}")
        except Exception as e:
            print(f"Erro ao calcular a expressão: {e}")


class WritingProcess(Process):
    def __init__(self, pid, expression):
        super().__init__(pid)
        self.expression = expression

    def execute(self):
        with open("computation.txt", "a") as f:
            f.write(self.expression + "\n")
        print(f"Expressão '{self.expression}' gravada com sucesso.")


class ReadingProcess(Process):
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list

    def execute(self):
        try:
            with open("computation.txt", "r") as f:
                lines = f.readlines()
            
            for line in lines:
                expression = line.strip()
                new_pid = len(self.process_list)  # Próximo PID disponível
                self.process_list.append(ComputingProcess(new_pid, expression))

            # Limpa o arquivo após a leitura
            open("computation.txt", "w").close()
            print("Leitura do arquivo concluída e processos adicionados.")
        except FileNotFoundError:
            print("Arquivo computation.txt não encontrado.")


class PrintingProcess(Process):
    def __init__(self, pid, process_list):
        super().__init__(pid)
        self.process_list = process_list

    def execute(self):
        print("Pool de processos:")
        for process in self.process_list:
            print(f"PID: {process.pid}, Tipo: {type(process).__name__}")


class ProcessPool:
    def __init__(self):
        self.process_list = []

    def create_process(self, process_type):
        pid = len(self.process_list)
        if process_type == "computing":
            expression = input("Digite a expressão: ")
            process = ComputingProcess(pid, expression)
        elif process_type == "writing":
            expression = input("Digite a expressão para gravar: ")
            process = WritingProcess(pid, expression)
        elif process_type == "reading":
            process = ReadingProcess(pid, self.process_list)
        elif process_type == "printing":
            process = PrintingProcess(pid, self.process_list)
        else:
            print("Tipo de processo inválido.")
            return
        
        self.process_list.append(process)
        print(f"Processo {process_type} criado com PID {pid}.")

    def execute_next(self):
        if self.process_list:
            process = self.process_list.pop(0)
            process.execute()
        else:
            print("Não há processos na fila.")

    def execute_specific(self, pid):
        for i, process in enumerate(self.process_list):
            if process.pid == pid:
                process.execute()
                del self.process_list[i]
                return
        print(f"Processo com PID {pid} não encontrado.")

    def save_to_file(self):
        with open("processes_state.txt", "w") as f:
            for process in self.process_list:
                f.write(f"{process.pid},{type(process).__name__}\n")
        print("Estado da fila de processos salvo em processes_state.txt.")

    def load_from_file(self):
        try:
            with open("processes_state.txt", "r") as f:
                for line in f:
                    pid, process_type = line.strip().split(',')
                    if process_type == "ComputingProcess":
                        expression = input(f"Digite a expressão para o PID {pid}: ")
                        self.process_list.append(ComputingProcess(int(pid), expression))
                    elif process_type == "WritingProcess":
                        expression = input(f"Digite a expressão para o PID {pid}: ")
                        self.process_list.append(WritingProcess(int(pid), expression))
                    elif process_type == "ReadingProcess":
                        self.process_list.append(ReadingProcess(int(pid), self.process_list))
                    elif process_type == "PrintingProcess":
                        self.process_list.append(PrintingProcess(int(pid), self.process_list))
            print("Fila de processos carregada com sucesso.")
        except FileNotFoundError:
            print("Arquivo de estado não encontrado.")


def main_menu():
    pool = ProcessPool()
    while True:
        print("\nMenu:")
        print("1. Criar Processo")
        print("2. Executar Próximo")
        print("3. Executar Processo Específico")
        print("4. Salvar Fila de Processos")
        print("5. Carregar Fila de Processos")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            process_type = input("Digite o tipo de processo (computing, writing, reading, printing): ")
            pool.create_process(process_type)
        elif choice == "2":
            pool.execute_next()
        elif choice == "3":
            pid = int(input("Digite o PID do processo a ser executado: "))
            pool.execute_specific(pid)
        elif choice == "4":
            pool.save_to_file()
        elif choice == "5":
            pool.load_from_file()
        elif choice == "6":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main_menu()

