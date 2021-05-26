//Program for understanding the different variables, their initialization and their scope

class Demo{
    int x=5;
    static int Y =10;
    int y=10;
    public static void main(String[] args) {
        Demo obj1 = new Demo();
        Demo obj2 = new Demo();
        obj1.x = obj1.x+2;
        obj1.y = obj1.y+2;
        System.out.println((obj1.x));
        System.out.println((obj1.y));
        System.out.println(obj2.x);
        System.out.println(obj2.y);
    }
}