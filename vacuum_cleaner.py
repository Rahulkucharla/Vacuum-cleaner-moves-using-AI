def Reflex_VACUUM_AGENT(location,status):
  if status=="Dirty":
    return "Suck"
  elif location=="A" and status=="Clean":
    return "Right"
  elif location=="B" and status=="Clean":
    return "Left"

print("----------------VACUUM CLEANER-------------------------")
print("Time taken for moving from one room to another room is 5secs")
print("Time taken for cleaning entire room is 10secs")
print("--------------------------------------------------------")
print("STATUS----\n 1.Clean\n 2.Dirty")
status_1=int(input("Enter status of Room A:"))
if status_1==1:
  status_A="Clean"
elif status_1==2:
  status_A="Dirty"
status_2=int(input("Enter status of Room B:"))
if status_2==1:
  status_B="Clean"
elif status_2==2:
  status_B="Dirty"
print("Location----\n1.ROOM A \n2.Room B")
curr=int(input("Enter Current Location of Vacuum Cleaner:"))
if curr==1:
  curr_loc="A"
elif curr==2:
  curr_loc="B"
cost=0
time=0
if curr_loc=="A":
  print("Vacuum cleaner is currently at Room A")
  if Reflex_VACUUM_AGENT("A",status_A)=="Suck":
    cost=cost+1
    time=time+10
    print("Room A is dirty")
    print("Cost for cleaning ROOM A",cost)
    print("----Cleaning Room A-----")
    print("Room A has been cleaned")
    status_A="Clean"
    print("Time taken for cleaning Room A",time,"secs")
    if Reflex_VACUUM_AGENT("B",status_B)=="Suck":
          print("Cleaner Moving From RoomA to RoomB")
          print("A---------->B")
          cost=cost+1
          print("Cost for moving from Room A to Room B",cost)
          time=time+5
          print("Time taken till now",time,"secs")
          print("Vacuum is currently at Room B")
          cost=cost+1
          time=time+10
          print("Room B is dirty")
          print("Cost for cleaning Room B",cost)
          print("Time taken ",time,"secs")
          status_B="Clean"
    elif Reflex_VACUUM_AGENT("B",status_B)=="Left":
          print("Room B is already clean")
          print("Cost ",cost)
  elif Reflex_VACUUM_AGENT("A",status_A)=="Right":
     print("Room A is already clean")
     cost=cost+0
     print("Cost ",cost)
     time=time+0
     print("Time taken for cleaning room A ",time,"secs")
     if Reflex_VACUUM_AGENT("B",status_B)=="Suck":
          print("Room B is dirty")
          print("Cleaner Moving From RoomA to RoomB")
          print("A---------->B")
          cost=cost+1
          print("Cost for moving from Room A to Room B ",cost)
          time=time+5
          print("Time taken till now ",time,"secs")
          print("Vacuum is currently at Room B")
          cost=cost+1
          time=time+10
          print("Cost for cleaning Room B",cost)
          print("Time taken",time,"secs")
          status_B="Clean"
     elif Reflex_VACUUM_AGENT("B",status_B)=="Left":
          print("Room B is already clean")
          print("Cost ",cost)
elif curr_loc=="B": #cleaner is in roomB
  print("Vacuum cleaner is currently at Room B")
  if Reflex_VACUUM_AGENT("B",status_B)=="Suck":#Room B is dirty
    cost=cost+1
    time=time+10
    print("Room B is dirty")
    print("Cost for cleaning ROOM B",cost)
    print("----Cleaning Room B-----")
    print("Room B has been cleaned")
    status_B="Clean"
    print("Time taken for cleaning Room B ",time,"secs")
    if Reflex_VACUUM_AGENT("A",status_A)=="Suck":#Room A is dirty
          print("Room A is dirty")
          print("Cleaner Moving From RoomB to RoomA")
          print("A<----------B")
          cost=cost+1
          print("Cost for moving from Room B to Room A",cost)
          time=time+5
          print("Time taken till now",time,"secs")
          print("Vacuum is currently at Room A")
          cost=cost+1
          time=time+10
          print("Cost for cleaning Room A",cost)
          print("Time taken",time,"secs")
          status_A="Clean"
    elif Reflex_VACUUM_AGENT("A",status_A)=="Right":#Room A is clean
          print("Room A is already clean")
          print("Cost",cost)
  elif Reflex_VACUUM_AGENT("B",status_B)=="Left":#Room B is clean
     print("Room B is already clean")
     cost=cost+0
     print("Cost",cost)
     time=time+0
     print("Time taken for cleaning room B",time,"secs")
     if Reflex_VACUUM_AGENT("A",status_A)=="Suck":#Room A is dirty
          print("Cleaner Moving From RoomB to RoomA")
          print("A<----------B")
          cost=cost+1
          print("Cost for moving from Room B to Room A ",cost)
          time=time+5
          print("Time taken till now",time,"secs")
          print("Vacuum is currently at Room A")
          cost=cost+1
          time=time+10
          print("Room A is dirty")
          print("Cost for cleaning Room A ",cost)
          print("Time taken %d",time,"secs")
          status_A="Clean"
     elif Reflex_VACUUM_AGENT("A",status_A)=="Right":#Room A is clean
          print("Room A is already clean")
          print("Cost ",cost)


if status_A=="Clean" and status_B=="Clean":
  print("Goal ACHIEVED")
  print("Both A and B are clean")
  print("Total cost of performance to complete task",cost)
  print("Total time taken to complete entire cleaning",time,"secs")






  

