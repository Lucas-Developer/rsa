#include "../unity.h"
#include "../rsa.h"
#include <stdlib.h>


void setUp()
{
}

void tearDown()
{
}

void primality_test(void)
{
    TEST_ASSERT(is_prime(3));
    TEST_ASSERT(!is_prime(4));
    TEST_ASSERT(is_prime(13));
}

int main(void) {

    UNITY_BEGIN();

    RUN_TEST(primality_test);

    return UNITY_END();
}

