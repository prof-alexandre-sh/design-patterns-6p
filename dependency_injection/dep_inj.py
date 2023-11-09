class CronJob:

    def __init__(self, schedule):
        self.schedule = schedule
        print("Criando cronjob")

    def run(self):
        print(f"Running job with schedule {self.schedule}")


class VM:

    def __init__(self, name, cron):
        ip = '000.000.000'
        self.name = name
        self.cron = cron # Injetamos a dependência

    def run_script(self):
        print(f"Rodando job na VM {self.name}")
        self.cron.run() # Dependência da classe CronJob

class VM_Setter:

    def __init__(self, name):
        ip = '000.000.000'
        self.name = name

    def set_job(self, job):
        self.job = job

    def run_script(self):
        print(f"Rodando job na VM {self.name}")
        self.job.run() # Dependência da classe CronJob

if __name__=="__main__":

    ### Invertemos o controle
    ### O controle de criação das classes agora fica no client

    ### Injetando dependência pelo construtor
    cron_job = CronJob("0 * * * *")
    vm_cron = VM("VM_Cron", cron_job) # Passamos o objeto como parâmetro no construtor
    #vm_cron.run_script()

    ### Injetando dependência com método setter
    vm_cron_set = VM_Setter("VM_Cron")
    vm_cron_set.set_job(cron_job)
    vm_cron_set.run_script()