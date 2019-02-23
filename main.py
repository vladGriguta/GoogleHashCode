import numpy as np
import pandas as pd

def readFile(file='a_example.in'):
    names = ['xStart','yStart','xFinish','yFinish','earliestStart','latestFinish']
    df = pd.read_csv(file,skiprows=[0],header=None,names=names,delimiter=' ')
    return df

def enoughTime(taxi,client,currentTime,max_time):
    if(taxi.distanceToClient(client['xStart'],client['yStart'])+client['distance'] < max_time-currentTime):
        return True
    else:
        return False


class taxi:
    def __init__(self,id_taxi):
        self.x = 0
        self.y = 0
        self.t = 0
        self.rides = []
        self.id = id_taxi
    def set_values(self,x,y,t):
        self.x = x
        self.y = y
        self.t = t
        
    def elapseTime(self):
        if(self.t>0):
            self.t -= 1
            
    def distanceToClient(self,xClient,yClient):
        return(np.abs(self.x-xClient)+np.abs(self.y-yClient))
    
    def assignRide(self,client_number):
        self.rides.append(client_number)
    
    def metricToClient(self,client,currentTime,bonus,max_time):
        # Check if trip is worthed
        if(self.distanceToClient(client['xStart'],client['yStart'])+client['distance']+currentTime > client['latestFinish']):
            return -1e5
        # check if customer can be taken to destination in time
        if(self.distanceToClient(client['xStart'],client['yStart'])+client['distance'] > max_time-currentTime):
            return -1e5
        #Compute and return the total number of points
        totalPoints = client['distance']
        if(self.distanceToClient(client['xStart'],client['yStart']) <= client['earliestStart']):
            totalPoints += bonus
        """
        else:
            totalPoints -= self.distanceToClient(client['xStart'],client['yStart'])
        """
        # time wasted to get to client
        #totalPoints -= self.distanceToClient(client['xStart'],client['yStart'])
        return totalPoints
    
    def pointsEarned(self,client,currentTime,bonus):
        if(self.distanceToClient(client['xStart'],client['yStart'])+client['distance']+currentTime > client['latestFinish']):
            return 0
        points = client['distance']
        if(self.distanceToClient(client['xStart'],client['yStart']) <= client['earliestStart']):
            points += bonus
        return points
        
    
        
def clientAssignment(matrix):
    n_rows,n_columns = np.shape(matrix)
    arrayOfElements = []
    for i in range(min(n_rows,n_columns)):
        #max_current = np.amax(matrix)
        max_pos = [0,0]
        max_current = matrix[0][0]
        for j in range(n_rows):
            for k in range(n_columns):
                if(matrix[j][k] > max_current):
                    max_pos = [j,k]
                    max_current = matrix[j][k]
        
        # SElect the position
        arrayOfElements.append(max_pos)
        
        # Convert all elements in line/column to -1
        matrix[max_pos[0]][:] = -1e6
        matrix[:,max_pos[1]] = -1e6
    return np.array(arrayOfElements)

def maxPoints(clients,bonus):
    points = float(bonus * len(clients))
    for i in range(len(clients)):
        points += clients['distance'].iloc[i]
    return points

if __name__ == "__main__":
    print('Functions imported   ')
    file = 'c_no_hurry.in'
    
    # Clear memory before doing the job
    import gc
    gc.collect()
    
    # Read generic parameters from file
    params = pd.read_csv(file,nrows=1,header=None,delimiter=' ')
    n_rows = int(params[0])
    n_columns = int(params[1])
    fleet = int(params[2])
    n_rides = int(params[3])
    bonus = int(params[4])
    max_time = int(params[5])
    
    # Read client list
    clients = readFile(file)
    clients['distance'] = np.abs(clients['xStart']-clients['xFinish']) + np.abs(clients['yStart']-clients['yFinish'])
    clients['id_client'] = [i for i in range(len(clients))]

    # initialize taxis
    taxis = [taxi(i) for i in range(fleet)]
    clients_local = []
    points = 0
    theoreticalMaxPoints = maxPoints(clients,bonus)
    
    percentage = 0
    for i in range(max_time):
        if(i%(max_time/100)==0):
            print('Progress is:    '+str(percentage)+' %')
            percentage += 1
        
        clients = clients.sort_values(by='earliestStart')        
        clients = clients.reset_index(drop=True)

        # Get free taxis
        free_taxis = []
        for j in range(fleet):
            if(taxis[j].t==0):
                free_taxis.append(taxis[j])
        
        """
        # Print clients assigned
        if(len(free_taxis) and len(clients)>0):
            print('Points earned so far......' + str(points))
            print('Clients left......'+str(len(clients)))
            print('The free taxis are:')
            for i in range(len(free_taxis)):
                print(free_taxis[i].id)
        """
        
        # Update list of clients to improve speed
        clients_local = clients[0:min(len(free_taxis)+50,len(clients))]
        
        matrixOfYield = np.zeros((len(free_taxis),len(clients_local)))
        
        # Compute a metric by which to sort taxis
        for j in range(len(free_taxis)):
            for k in range(len(clients_local)):
                matrixOfYield[j][k] = free_taxis[j].metricToClient(clients_local.iloc[k][:],i,bonus,max_time)
        
        # Sort taxis by metric and assign clients to taxis
        list_assigned = clientAssignment(matrixOfYield)
        
        indexes_to_drop = []
        # Now assign customers to taxis
        for j in range(len(list_assigned)):
            
            # Identify taxy[j]
            for k in range(len(taxis)):
                if(taxis[k].id==free_taxis[j].id):

                    # Keep taxis busy
                    # need to always consider full list of clients
                    taxis[k].t = taxis[k].distanceToClient(clients_local['xStart'].iloc[list_assigned[j][1]],
                         clients_local['yStart'].iloc[list_assigned[j][1]]) + clients_local['distance'].iloc[list_assigned[j][1]]
                    # assign ride to taxy
                    taxis[k].assignRide(clients_local['id_client'].iloc[list_assigned[j][1]])
                    #print('Taxi '+str(taxis[k].id)+' was assigned to client '+str(clients_local['id_client'].iloc[list_assigned[j][1]]))
                    points += taxis[k].pointsEarned(clients_local.iloc[list_assigned[j][1]][:],i,bonus)
            indexes_to_drop.append(list_assigned[j][1])
            
        
        #print(clients)
        #print(indexes_to_drop)
        clients = clients.drop(index=indexes_to_drop)
        clients_local = clients_local.drop(index=indexes_to_drop)


            
        # elapse time
        for j in range(len(taxis)):
            taxis[j].elapseTime()
            
        
            
    # Print list of orders
    file_output=open(file[:-3]+".out", "w",encoding='ASCII')
    
    for i in range(len(taxis)):
        #print(str(taxis[i].id)+' '+str(taxis[i].rides))
        file_output.write(str(taxis[i].id)+' '+str(len(taxis[i].rides))+'')
        for j in range(len(taxis[i].rides)):
            file_output.write(' '+str(taxis[i].rides[j]))
        file_output.write('\n')
    file_output.close()
    
    
    print('The efficiency is:    '+str(100*points/theoreticalMaxPoints)+' %')
    
        
        
        