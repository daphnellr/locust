import time
from typing import Optional, Tuple, List, Type, Union

from . import User
from .runners import Runner


class LoadTestShape:
    """
    A simple load test shape class used to control the shape of load generated
    during a load test.
    """

    runner: Optional[Runner] = None
    """Reference to the :class:`Runner <locust.runners.Runner>` instance"""

    def __init__(self):
        self.start_time = time.perf_counter()

    def reset_time(self):
        """
        Resets start time back to 0
        """
        self.start_time = time.perf_counter()

    def get_run_time(self):
        """
        Calculates run time in seconds of the load test
        """
        return time.perf_counter() - self.start_time

    def get_current_user_count(self):
        """
        Returns current actual number of users from the runner
        """
        return self.runner.user_count

    def tick(self) -> Union[Tuple[int, float], Tuple[int, float, Optional[List[Type[User]]]], None]:
        """
        Returns a tuple with 2 elements to control the running load test:

            user_count -- Total user count
            spawn_rate -- Number of users to start/stop per second when changing number of users
            user_classes -- None or a List of userclasses to be spawned in it tick
        If `None` is returned then the running load test will be stopped.

        """

        return None
