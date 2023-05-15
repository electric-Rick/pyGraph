import numpy as np
import matplotlib.pyplot as plt


class Mola():        
    def __init__(self):
        pass
    
    def grande(self):
        T_grande = np.array([0.33, 0.65, 0.98, 1.31, 1.63])
        return [x/10 for x in T_grande]


    def pequena(self):
        T_pequena = np.array([1.5, 2.0, 3.0, 4.2, 5.1])
        return [x/10 for x in T_pequena]
        

class Graph():
    def __init__(self):
        pass
    
    def presentation(self):        
        massas =np.array([50.0, 100.1,150.1, 200.1,250.5])
        mola = Mola()
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        ax1.plot(mola.pequena(), [(massa/1000)*9.8 for massa in massas], color='blue', label='Mola Pequena', linestyle='--', marker='o')
        ax2.plot(mola.grande(), [(massa/1000)*9.8 for massa in massas], color='red', label='Mola Grande', linestyle='--', marker='o')
        ax1.set_xlabel('Deformação (cm/10)')
        ax1.set_ylabel('Massa (Newton)')
        ax1.set_title('Massa x Deformação (mola pequena)')
        ax2.set_xlabel('Deformação (cm/10)')
        ax2.set_ylabel('Massa (Newton)')
        ax2.set_title('Massa x Deformação (mola grande)')
        plt.show()
    
        
    
    

