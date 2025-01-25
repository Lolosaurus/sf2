stream = int(input('How many streams?: '))
flow = []
while stream != 0:
    ask = int(input('What is the flow of this stream?: '))
    flow.append(ask)
    stream -= 1
action = int(input('What happens? (99 to split, 88 to merge, 77 to finish): '))
def split():
    num = int(input('What stream do you want to split?: '))
    percent = int(input('what percent of the flow splits off?: '))
    flow.insert(num-1, flow[(num-1)]*(percent*0.01))  
    flow[num] = flow[(num)]*(1-(percent*0.01))
def merge():
    num = int(input('What stream do you want to merge?: '))
    flow[num-1] = flow[num-1]+flow[num]
    del flow[num]
while action != 77:
    if action == 99:
        split()
    else:
        merge()
    action = int(input('What happens? (99 to split, 88 to merge, 77 to finish): '))
print(flow)