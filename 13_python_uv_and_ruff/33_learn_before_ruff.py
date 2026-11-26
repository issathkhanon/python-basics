import random, json
import sys

def save_random_scores(filename, count):
    # 1. Missing 'with open' (SIM115) & missing encoding (PLW1514)
    file = open(filename, "w")
    
    try:
        scores = [random.randint(1, 100) for _ in range(count)]
        for score in scores:
            # 2. Nested 'if' statements (SIM102)
            if score > 50:
                if score % 2 == 0:
                    file.write(f"High even score: {score}\n")
                    
        if len(scores) == 0:
            # 3. Raising vanilla Exception & long message inline (TRY002, TRY003)
            raise Exception("No random scores were generated for the output file")
            
    # 4. Blind/broad exception catching & re-raising without 'from' (BLE001, B904)
    except Exception as e:
        print(f"Failed: {e}")
        raise RuntimeError("Logging failed")
    finally:
        file.close()
