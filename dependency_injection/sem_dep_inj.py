class CronJob:

    def __init__(self, schedule):
        self.schedule = schedule
        print("Criando cronjob")

    def run(self):
        print(f"Running job with schedule {self.schedule}")


class VM:

    def __init__(self, name):
        ip = '000.000.000'
        self.name = name

    def run_script(self):
        job = CronJob("0 * * * *")
        print(f"Rodando job na VM {self.name}")
        job.run() # Dependência da classe CronJob

if __name__=="__main__":

    vm_cron = VM("VM_Cron")
    vm_cron.run_script()