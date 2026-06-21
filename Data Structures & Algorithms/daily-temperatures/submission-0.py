class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        counter = 0
        temp = 0
        finish = []

        while temperatures:
            temp = temperatures.pop(0)
            counter = 0

            for future_temp in temperatures:
                counter += 1

                if future_temp > temp:
                    finish.append(counter)
                    break
            else:
                finish.append(0)

        return finish
            



        return finish
