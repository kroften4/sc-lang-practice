export function shuffledArray(arr: any[]): any[] {
    return arr.toSorted(function(a, b) {
        return Math.random() - 0.5;
    });
}

export function shuffleArray(arr: any[]): void {
    arr.sort(function(a, b) {
        return Math.random() - 0.5;
    });
}

export function randIndex(arr: any[]): number | null {
    if (arr.length == 0) {
        return null;
    }
    return Math.floor(Math.random() * arr.length)
}
