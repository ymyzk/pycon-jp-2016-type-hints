<?php
function greeting($name) {
    return "Hello, " . $name;
}
function main() {
    greeting("Taro");
    greeting(12345);
}
main();
