#include "internal.h"

bool is_prime(unsigned int candidate)
{
    for (unsigned int i=2; i < candidate ; i++) {
        if (candidate  % i == 0) {
            return false;
        }
    }
    return true;
}
