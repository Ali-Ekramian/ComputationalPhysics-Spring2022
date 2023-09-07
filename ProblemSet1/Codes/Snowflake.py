import numpy as np
import matplotlib.pyplot as plt
line = np.array([[0, 0], [1, 0]])
angle = np.pi / 3
R = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
def op(obj):
    obj1 = obj / 3
    rotated_obj1 = np.dot(R, obj1.T).T 
    translation_vector1 = np.array([1/3, 0])
    obj2 = rotated_obj1 + translation_vector1
    pre_translation_vector = -np.array([1/3, 0])
    pre_translated_obj = obj1 + pre_translation_vector
    rotated_obj = np.dot(R.T, pre_translated_obj.T).T
    translation_vector = np.array([2/3, 0])
    obj3 = rotated_obj + translation_vector
    translation_vector2 = np.array([2/3, 0])
    obj4 = obj1 + translation_vector2
    ans = np.array([obj1,obj2,obj3,obj4])
    print(ans,"ans")
    return ans
def snow(n):
    if n<1:
        return line
    else:
        a = op(snow(n-1))
        return a
ans = snow(1)
obj1 = ans[0]
obj2 = ans[1]
obj3 = ans[2]
obj4 = ans[3]
plt.plot(obj1[:,0],obj1[:,1])
plt.plot(obj2[:,0],obj2[:,1])
plt.plot(obj3[:,0],obj3[:,1])
plt.plot(obj4[:,0],obj4[:,1])
plt.legend()
plt.show()


