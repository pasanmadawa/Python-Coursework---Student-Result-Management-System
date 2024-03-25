# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1956442 
 
# Date: 14th december 2022 

count1 = 0
count2 = 0
count3 = 0
count4 = 0
list1 = []

    
while True:
    
    def int_input(input_message):
     
        while True:
            try:
                inputs = int(input(input_message))
               

            except ValueError:
                print('Integer required')
                continue
            if inputs > 120:
                print('Out of range')
            elif inputs % 20 != 0:
                print('Out of range')
            else:
            
                return inputs
  
       
    passes = int_input('Enter your credits at pass: ')
    defer = int_input('Enter your credits at defer: ')
    fail = int_input('Enter your credits at fail: ')

    total = passes + defer + fail
    
    if total != 120:
        print('Total incorrect.\n')
        continue
 
    
    if passes == 120 and defer == 0 and fail == 0 : # 1st line

        print('progress')

        result = f"progress - {passes}, {defer}, {fail}"
        count1 += 1


    elif passes == 100 and 0<= defer <= 20 and 0 <= fail <= 20 : # 2nd and 3rd lines
    
        print('Progress(module trailer)')
        result = f"'Progress(module trailler) - {passes}, {defer}, {fail}"
        count2 += 1


    elif passes == 80 and 0 <= defer <= 40 and 0 <= fail <= 40: # 4th to 6th lines
        
        print('Module retriever')
        result = f"Module retriever - {passes}, {defer}, {fail}"
        count3 += 1
    
    
    elif passes == 60 and 0 <= defer <= 60 and 0 <= fail <= 60 : # 7th to 10th lines
        
        print('Module retriever')
        result = f"Module retriever - {passes}, {defer}, {fail}"
        count3 += 1
    
    
    elif passes == 40 and 20 <= defer <= 80 and 0 <= fail <= 60: # 11th to 14th lines
        
        print('Module retriever')
        result = f"Module retriever - {passes}, {defer}, {fail}"
        count3 += 1

   
    elif passes == 40 and defer == 0 and fail == 80 : # 15th line
   
        print('Exclude')
        result = f"Exclude - {passes}, {defer}, {fail}"
        count4 += 1 
 
   
    elif passes == 20 and 40 <= defer <= 100 and  0 <= fail <= 60: # 16th to 19th lines
       
        print('Module retrive')
        result = f"Module retriever - {passes}, {defer}, {fail}"
        count3 += 1
    
 
    elif passes == 20 and 0 <= defer <= 20 and 80 <= fail <= 100: # 20th and 21st lines
       
        print('Exclude')
        result = f"Exclude - {passes}, {defer}, {fail}"
        count4 += 1
    
   
    elif passes == 0 and 60 <= defer <= 120 and 0 <= fail <= 60: # 22nd to 25th lines
        
        print('Module retrive')
        result = f"Module retriever - {passes}, {defer}, {fail}"
        count3 += 1
    
   
    elif passes == 0 and 0 <= defer <= 40 and 80 <= fail <= 120: # 26th to 28th lines
       
        print('Exclude')
        result = f"Exclude - {passes}, {defer}, {fail}"
        count4 += 1

  
    list1.append(result)
    print('\nWould you like to enter another set of data? ')
    

    while True:
        try:
            conti = str(input("Enter 'y' for yes or 'q' to quit and view results: ")).lower()
            if conti != 'y' and conti != 'q':
                print(' Please input correct value')
                continue
        except ValueError:
            print('Invalid inputs')
 
        break

    if conti == 'y':
        print('\n')
        continue
        
    if conti == 'q':
        
       
        
        print('-------------------------------------------------')
        print('\nHistogram')

        print('Progress ' , count1 , ' : ', count1 * " * ")
        print('Trailer  '  , count2 , ' : ', count2 * " * ")
        print('Retriever' , count3 , ' : ', count3 * " * ")
        print('Excluded ' , count4 , ' : ', count4 * " * ",'\n')

        print( count1 + count2 + count3 + count4, 'outcomes in total.')
        print('-------------------------------------------------')
        print("Part 2:\n")
        for i in list1:
            print(i)

            
    break
