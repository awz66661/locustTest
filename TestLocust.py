import datetime
import math
from locust import HttpUser, task, between, LoadTestShape, FastHttpUser


class Tasks(FastHttpUser):
    wait_time = between(1, 5)

    @task
    def test_task(self):
        self.client.get("/v3/weather/weatherInfo?city={{adcode}}&key=19d1f2b8c543ccf668f6364239ea836a")

class MyCustomShape(LoadTestShape):
    use_common_options = True
    # time_limit设置时限整个压测过程为60秒
    time_limit = 300
    # 设置产生率一次启动10个用户
    spawn_rate = 10
    # 设置tick()函数
    def tick(self):
        '''
        设置 tick()函数
        并在tick()里面调用 get_run_time()方法
        '''
    # 调用get_run_time()方法获取压测执行的时间
        run_time = self.get_run_time()
        # 运行时间在 time_limit之内，则继续执行
        if run_time < self.time_limit:
            # user_count计算每10秒钟增加10个
            user_count = 10*round(run_time, -1)
            print(str(user_count)+">>>>>"+datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f'))
            return (user_count, self.spawn_rate)

        # 运行时间超过time_limit，则停止
        return None
