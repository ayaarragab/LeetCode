class Solution {
public:
    double fastPow(double x, long long n) {
        if (n == 0)
            return 1;

        double half = fastPow(x, n / 2);

        if (n % 2)
            return half * half * x;

        return half * half;
    }

    double myPow(double x, int n) {
        long long power = n;

        if (power < 0)
            return 1.0 / fastPow(x, -power);

        return fastPow(x, power);
    }
};