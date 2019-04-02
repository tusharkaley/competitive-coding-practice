import java.util.logging.*;
public class JavaLogging {

    private static Logger logger;


    public static void main(String[] args) {
        

        try{
            JavaLogging jl = new JavaLogging();
            jl.setUpLogger(Integer.parseInt(args[0]));
            logger.entering("main method", "doIt");
            logger.info("Logging done");
        } catch (Exception e) {
            e.printStackTrace();
        }

        logger.exiting("main method", "doIt");
    }
    public void setUpLogger(int peerID){
        try{
            System.setProperty("java.util.logging.SimpleFormatter.format",
              "[%1$tF %1$tT] [%4$-7s] %5$s %n");
            logger = Logger.getLogger("log_peer_"+peerID);
            FileHandler fh;
            fh = new FileHandler("log_peer_"+peerID+".log");
            logger.addHandler(fh);

            SimpleFormatter formatter = new SimpleFormatter();

            fh.setFormatter(formatter);
            } catch (Exception e) {
            logger.log(Level.SEVERE, "Error doing XYZ", e);
        }

           
    }

}