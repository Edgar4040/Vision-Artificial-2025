import cv2
import matplotlib.pyplot as plt
import numpy as np


import cv2
import matplotlib.pyplot as plt
import numpy as np


import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('mainlogo.png', cv2.IMREAD_GRAYSCALE)


img_eq = cv2.equalizeHist(img)


histx1 = cv2.calcHist([img], [0], None, [256], [0, 256])
histx2 = cv2.calcHist([img_eq], [0], None, [256], [0, 256])


histy1 = np.sum(img, axis=0)
histy2 = np.sum(img_eq, axis=0)


fig = plt.figure(figsize=(14, 6))
gs = fig.add_gridspec(3, 4)


ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(histx1, color='black')
ax1.set_title('Histograma X - Original')
ax1.set_xlim([0, 256])
ax1.set_xticks([])
ax1.set_yticks([])


ax2 = fig.add_subplot(gs[0, 2])
ax2.plot(histx2, color='black')
ax2.set_title('Histograma X - Ecualizada')
ax2.set_xlim([0, 256])
ax2.set_xticks([])
ax2.set_yticks([])


ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(histy1, color='black')
ax3.set_title('Histograma Y - Original')
ax3.set_ylim([0, np.max(histy1)])
ax3.set_yticks([])
ax3.set_xticks([])


ax4 = fig.add_subplot(gs[1, 1])
ax4.imshow(img, cmap='gray')
ax4.set_title('Imagen Original')
ax4.axis('off')


ax5 = fig.add_subplot(gs[1, 2])
ax5.plot(histy2, color='black')
ax5.set_title('Histograma Y - Ecualizada')
ax5.set_ylim([0, np.max(histy2)])
ax5.set_yticks([])
ax5.set_xticks([])


ax6 = fig.add_subplot(gs[1, 3])
ax6.imshow(img_eq, cmap='gray')
ax6.set_title('Imagen Ecualizada')
ax6.axis('off')

plt.tight_layout()
plt.show()
