public class timer {
  public static void main(String[] args){
    // start time
    long startTime = System.currentTimeMillis(); 

    try {
      Thread.sleep(1000);
    } catch (InterruptedException e){
      e.printStackTrace();
    }

    // end time
    long endTime = System.currentTimeMillis(); 
    // calculate duration 
    long combTime = endTime - startTime;

    System.out.println(combTime);

  }
}
