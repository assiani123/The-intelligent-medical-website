import { TestBed } from '@angular/core/testing';

import { GardpGuard } from './gardp.guard';

describe('GardpGuard', () => {
  let guard: GardpGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(GardpGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
