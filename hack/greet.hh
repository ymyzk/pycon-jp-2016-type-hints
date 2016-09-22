<?hh
function greeting(string $name): string {
    return "Hello, " . $name;
}
function main(): void {
    greeting("Taro");
    greeting(12345);
}
main();