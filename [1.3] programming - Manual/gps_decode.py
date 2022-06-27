from collections import defaultdict

dict_rsp = defaultdict(int)
dict_rsp_cmds = defaultdict(set)

with open('GPS_Instructions.txt') as manual:
	instructions = manual.readlines()
	for instruction in instructions:
		command, arg1, arg2 = instruction.split()
		print(command, arg1, arg2)

		if arg2.isalpha():
			arg2_value = dict_rsp[arg2]
		else:
			arg_2value = int(arg2)

		arg1_value = dict_rsp[arg1]
		arg2_value = dict_rsp[arg2] if arg2.isalpha() else int(arg2)

		if command == "ADD":
			dict_rsp[arg1] = arg1_value + arg2_value
			dict_rsp_cmds[arg1].add('ADD')
		if command == "MUL":
			dict_rsp[arg1] = arg1_value * arg2_value
			dict_rsp_cmds[arg1].add('MUL')
		if command == 'EXCH':
			if arg2.isalpha():
				dict_rsp[arg1], dict_rsp[arg2] = dict_rsp[arg2], dict_rsp[arg1]
			else:
				dict_rsp[arg1] = arg2_value
			dict_rsp_cmds[arg1].add('EXCH')
		if command == 'DIV':
			dict_rsp[arg1] = arg1_value // arg2_value
			dict_rsp_cmds[arg1].add('DIV')
		if command == 'MOD':
			dict_rsp[arg1] = dict_rsp[arg1] % arg2_value
			dict_rsp_cmds[arg1].add('MOD')
		if command == 'EQL':
			if dict_rsp[arg1] == dict_rsp[arg2]:
				dict_rsp[arg1] = 1
			else:
				dict_rsp[arg1] = 0
			dict_rsp_cmds[arg1].add('EQL')

print(dict_rsp)

for k in sorted(dict_rsp.keys()):
	print(f"{k}: {chr(dict_rsp[k])}")
