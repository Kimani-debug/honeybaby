import java.util.Scanner;
/**
 * input
 */
public class input {

    public static void main(String[] args) {
        
            
        
        System.out.println("hey welcome to finance app");
        System.out.println("lets get started by getting your name");
        try (Scanner myObjsScanner = new Scanner(System.in)) {
            String userName = myObjsScanner.nextLine();
            System.out.println("hi " + userName + " glad you could make it");
        
        
        /**
         * give options (saving suggestions)
         * expense input?
         * 
         * theres 50 30 20
         */
        System.out.println(" choose a option");
        System.out.println("'1' to see name options");
        System.out.println("'2' to input expenses");
        System.out.println("'3' to enter income");
        System.out.println("'4' to see saving recomendations");
        int choice = myObjsScanner.nextInt();
        String newNameString = myObjsScanner.nextLine();
                
    
        switch (choice){
            case 1 : 
            System.out.println("hi you chose to update your name, currently it is " + userName);
            System.out.println("would you like to change it?");
            System.out.println("'yes' or 'no'");
            String choiceString = myObjsScanner.next();
            switch (choiceString) {
                case "Yes":
                case "yes":
                    System.out.println("okay what would you want to change it to?");
                    newNameString = myObjsScanner.next();
                    userName = newNameString;
                    System.out.println("okay , it is now " + userName + " welcome again");
                    break;                 
            
                case "No":
                case "no":
                    break;
                default:
                    break;
            }
            break;
            case 2: 
            System.out.println("okay you chose to input some expenses");
            System.out.println("ready?");
            System.out.println("'yes' when you're ready.");
            choiceString = myObjsScanner.next();
            
            switch (choiceString) {
                case "Yes":
                case "yes":
                System.out.println("lets start adding it up then");
                System.out.println("whats the first expense?");
                int expense = myObjsScanner.nextInt();
                System.out.println("so far you have " + expense + " any more?");
                    switch (choiceString) {
                    case "yes":
                        System.out.println("whats the second expense?");
                        int newExpense = myObjsScanner.nextInt();
                        expense = (newExpense + expense);
                        System.out.println("your new expense amount is now " + expense);
                        break;
                
                    default:
                        break;
                }
                
                    break;
            
                default:
                    break;
            }
            
                  


            

            break;
            default : System.out.println("invalid input sorry");    
        }
    }
    }
}
