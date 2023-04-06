package BusinessLayer;

import java.util.ArrayList;

public class BalanceSheet extends Report { //implements IAccountancy, ICalculable {

    /**
     * public void threadExample(MyInterface someMethod){ // implements a method of type `MyInterface`
     * <p>
     * new Thread(() ->
     * someMethod()).
     * start(); //this::someMethod) //error; thread container is not a functional interface
     * <p>
     * //.Thread(MyFunction)
     * //  start();
     * // void start() {
     * // }
     * }
     *
     * @Contract(pure = true)
     * private @Nullable Object someMethod() {
     * return null;
     * }
     */

    //@Override
    public static void printFunction() {
    }

    class currentNonCurrent {

        private ArrayList<String> names = new ArrayList<>();
        private ArrayList<Double> prices = new ArrayList<>();

        public currentNonCurrent() {
            ArrayList<String> names = new ArrayList();
            ArrayList<Double> prices = new ArrayList();
        }

        public currentNonCurrent(ArrayList<String> names, ArrayList<Double> prices) {
            this.names = names;
            this.prices = prices;
        }
    }

    class namesPrices {
        private ArrayList<String> names = new ArrayList<>();
        private ArrayList<Double> prices = new ArrayList<>();

        public namesPrices() {
            ArrayList<String> names = new ArrayList();
            ArrayList<Double> prices = new ArrayList();
        }

        public namesPrices(ArrayList<String> names, ArrayList<Double> prices) {
            this.names = names;
            this.prices = prices;
        }
    }
}
