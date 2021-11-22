import h5py
import numpy as np
from PIL import Image
path = "train/"
keys = ['height', 'label', 'left', 'top', 'width']
import shapely.geometry
import os
def translate(arr):
	s = ''
	for i in arr:
		s += chr(i[0])
	return s
def get_names_inorder(path):
    f = os.listdir(path)
    new_f = []
    for name in f:
        s = name[:-4]
        new_f.append(int(s))
    new_f.sort()
    f.clear()
    for name in new_f:
        name = str(name) + ".png"
        f.append(name)
    return f
def get_segmentation(left,top,width,height):
    polygon=shapely.geometry.box(*(left,top,left+width, top+height), ccw=True)   
    K=str(polygon.wkt).split("POLYGON ((")[-1].split("))")[0].split(',')
    polygon=[]
    for m in K:
        for p in m.split(" "):
            if p:
                polygon.append(int(p))
    return polygon	
def make_names(mat):
	names = []
	for n_arr in mat['/digitStruct/name']:
		for ref in n_arr:
			name = translate(np.array(mat[ref]))
			names.append(name)
	return names

def make_bboxes(mat):
	bboxes = {}

	size = mat['/digitStruct/bbox'].shape[0]
	checker = np.zeros(2, dtype='float64')
	checker = type(checker[0])
	for key in keys:
		print(key)
		bboxes[key] = []
		#cnt = 0
		for n_arr in mat['/digitStruct/bbox']:
			#print(cnt)
			for ref in n_arr:
				grp = mat[ref]
				set = grp[key]
				result = []
				for nd_arr in set:
					for real_ref in nd_arr:
						if checker == type(real_ref):
							#print('Label: {}, value:{} \n'.format(key, np.array(real_ref)))
							result.append(int(real_ref))
						else:
							#print('Label: {}, value: {} \n'.format(key,np.array(mat[real_ref],dtype='float64')))
							result.append(int(np.array(mat[real_ref])))
				#if len(result) > 1:
					#print('Label {}, Result: {}'.format(key, result))
				#print(result)
				bboxes[key].append(result)
				#print(bboxes[key])
			#cnt += 1
	#print('Result: {}'.format(bboxes))
	return bboxes

def gen_labels(names,bboxes,P):
    print('gen coco file')
    size = len(bboxes['label'])
    
    cnt = 0
    for i in range(size):
        img = Image.open(path+names[i]).convert("RGB")
        
        file_name = P + names[i][:-4]+ ".txt"
        f = open(file_name,'w')
        sub_size = len(bboxes['label'][i])
        
        for j in range(sub_size):
            cate = bboxes['label'][i][j]
            if cate == 10:
                cate = 0
            width = bboxes['width'][i][j]
            height = bboxes['height'][i][j]
            x_center = bboxes['left'][i][j] + (width / 2)
            y_center = bboxes['top'][i][j] + (height / 2)
            
            width /= img.width
            height /= img.height
            x_center /= img.width
            y_center /= img.height
            f.write(str(cate))

            f.write(" " + str(x_center))
            
            f.write(" " + str(y_center))
            
            f.write(" " + str(width))

            f.write(" " + str(height))

            f.write('\n')

    return

mat = h5py.File(path + 'digitStruct.mat', 'r')
if os.path.isdir('./labels/') is not True:
    os.makedirs('./labels/')

# dealing names

print('Holding for names')

names = make_names(mat)
#print(names)

print('names dealt done')

print('Holding for bboxes')

bboxes = make_bboxes(mat)
print('bboxes dealt done')

#for i in range(len(bboxes['label'])):
#	print('Image: {},  Number: {}\n'.format(names[i],bboxes['label'][i]))
print('generating labels')
gen_labels(names,bboxes,'./labels/')

