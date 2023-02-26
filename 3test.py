

def open_dict(filename):
	with open("result.txt", "w", encoding="UTF-8") as d:
		basic_dict = {}
		for i in filename:
			with open(i, encoding="UTF-8") as f: a = f.readlines()
			basic_dict[i] = len(a)
		for keys, values in sorted(basic_dict.items(), key=lambda item: item[1]):
			d.writelines(f'{keys}\n{str(values)}\n')
			for line in open(keys, encoding="UTF-8"): d.writelines(line)
			d.writelines('\n')


list_1 = ["text1.txt", "text2.txt", "text3.txt"]
open_dict(list_1)
